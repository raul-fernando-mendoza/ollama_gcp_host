select  
       t.table_name || '.' ||
       c.column_name || ' ' ||
       c.data_type
from information_schema.tables t
inner join information_schema.columns c on 
         c.table_schema = t.table_schema and c.table_name = t.table_name
--where table_type = 'FACT_FIT_STAT_MEMBER_DETAILS'    
where t.table_schema = 'DA_DW'
order by t.table_schema,
       t.table_name,
       ordinal_position;
