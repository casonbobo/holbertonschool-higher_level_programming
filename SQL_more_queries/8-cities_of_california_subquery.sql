-- This is not a comment
SELECT id, state FROM cities WHERE state_id = ( 
    SELECT id FROM states WHERE state = 'California'
);
