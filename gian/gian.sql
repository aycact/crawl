CREATE TABLE test(
    id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
    name STRING NOT NULL,
    age INT NOT NULL
);
CREATE PROCEDURE insert_test(pn STRING, pa INT)
LANGUAGE SQL
AS $$
    INSERT INTO test(name, age) VALUES(pn, pa);
$$;
CALL insert_test('Gian', 20);
SELECT * FROM test;