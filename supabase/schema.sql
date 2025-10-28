
-- Run this in your Supabase SQL editor

-- Profiles table (1:1 with auth.users)
create table if not exists public.profiles (
  id uuid primary key references auth.users (id) on delete cascade,
  display_name text,
  role text default 'user',
  created_at timestamp with time zone default now()
);

alter table public.profiles enable row level security;
create policy "profiles_read_any" on public.profiles for select using (true);
create policy "profiles_self_insert" on public.profiles for insert with check (auth.uid() = id);
create policy "profiles_self_update" on public.profiles for update using (auth.uid() = id);

-- Auto-create profile on signup
create or replace function public.handle_new_user()
returns trigger as $$
begin
  insert into public.profiles (id, display_name)
  values (new.id, coalesce(new.raw_user_meta_data->>'display_name', ''));
  return new;
end;
$$ language plpgsql security definer;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();

-- Platform accounts linked to user
create table if not exists public.platform_accounts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references public.profiles (id) on delete cascade,
  platform text check (platform in ('youtube','twitch','chzzk','sooptv')) not null,
  external_id text not null,
  url text,
  verified boolean default false,
  verified_at timestamp with time zone,
  created_at timestamp with time zone default now()
);

alter table public.platform_accounts enable row level security;
create policy "pa_select_own_or_public" on public.platform_accounts
  for select using (auth.uid() = user_id);
create policy "pa_insert_own" on public.platform_accounts
  for insert with check (auth.uid() = user_id);
create policy "pa_update_own" on public.platform_accounts
  for update using (auth.uid() = user_id);

-- Admins can verify (optional: create a 'service_role' or use SQL editor)
-- update public.profiles set role='creator_verified' where id='...';
-- update public.platform_accounts set verified=true, verified_at=now() where id='...';
