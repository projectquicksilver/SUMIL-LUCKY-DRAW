import { createClient } from '@supabase/supabase-js';

const SUPABASE_URL = 'https://zmjheixjfwbbixptveie.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InptamhlaXhqZndiYml4cHR2ZWllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODQ1MTg3OTIsImV4cCI6MjEwMDA5NDc5Mn0.U9mBHdIryo7RPhnbFemurfrhrjKV7pngD8vC-sfjjSA';
const SUPABASE_SERVICE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InptamhlaXhqZndiYml4cHR2ZWllIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4NDUxODc5MiwiZXhwIjoyMTAwMDk0NzkyfQ.0HzNeGXdw0GFNrTtJpUNz2RSlaKgaVTlodpGEtdqWBE';

// The regular client for the public UI (safe to expose)
export const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

// The admin client for the dashboard (DANGEROUS: Do not expose to public routes!)
export const supabaseAdmin = createClient(SUPABASE_URL, SUPABASE_SERVICE_KEY);
