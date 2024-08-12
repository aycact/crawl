CREATE TABLE test(
    id UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
    name STRING NOT NULL,
    age INT NOT NULL
);
CREATE PROCEDURE insert_test(name STRING, age INT) AS 
$$
DECLARE
    pname STRING;
    page INT;
BEGIN
    INSERT INTO test(name, age) VALUES(pname, page);
END;
$$ LANGUAGE SQL;