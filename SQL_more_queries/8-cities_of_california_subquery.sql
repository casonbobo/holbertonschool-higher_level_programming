-- This is not a comment
SELECT id, name FROM cities WHERE state_id = ( 
    SELECT id FROM cities WHERE state = 'California';
);
