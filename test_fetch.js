import { createClient } from '@supabase/supabase-js';

const supabaseAdmin = createClient(
  'https://zmjheixjfwbbixptveie.supabase.co',
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InptamhlaXhqZndiYml4cHR2ZWllIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4NDUxODc5MiwiZXhwIjoyMTAwMDk0NzkyfQ.0HzNeGXdw0GFNrTtJpUNz2RSlaKgaVTlodpGEtdqWBE'
);

async function test() {
  let allCustomers = [];
  let page = 0;
  const limit = 1000;

  while (true) {
    const { data: customersChunk, error: fetchErr } = await supabaseAdmin
        .from('master_customers')
        .select('*')
        .gt('sum_of_max_coupons', 0)
        .range(page * limit, (page + 1) * limit - 1);
    
    if (fetchErr) {
        console.error(fetchErr);
        break;
    }

    if (customersChunk && customersChunk.length > 0) {
      allCustomers = [...allCustomers, ...customersChunk];
      console.log(`Page ${page}: Fetched ${customersChunk.length} rows`);
    }

    if (!customersChunk || customersChunk.length < limit) {
      break; 
    }
    page++;
  }
  console.log(`Total fetched without order: ${allCustomers.length}`);

  let allCustomersOrdered = [];
  page = 0;
  while (true) {
    const { data: customersChunk, error: fetchErr } = await supabaseAdmin
        .from('master_customers')
        .select('id') // just select id to speed up
        .gt('sum_of_max_coupons', 0)
        .order('id', { ascending: true })
        .range(page * limit, (page + 1) * limit - 1);
    
    if (fetchErr) {
        console.error(fetchErr);
        break;
    }

    if (customersChunk && customersChunk.length > 0) {
        allCustomersOrdered = [...allCustomersOrdered, ...customersChunk];
    }

    if (!customersChunk || customersChunk.length < limit) {
      break; 
    }
    page++;
  }
  console.log(`Total fetched with order: ${allCustomersOrdered.length}`);
}

test();
