CREATE TABLE loans (
  loan_id SERIAL PRIMARY KEY,
  applicant_income NUMERIC,
  loan_value NUMERIC,
  owner_occupied BOOLEAN,
  denial_reason TEXT
);

INSERT INTO loans (applicant_income, loan_value, owner_occupied, denial_reason) VALUES
(55000, 200000, TRUE, NULL),
(45000, 150000, TRUE, 'Insufficient credit history'),
(30000, 250000, FALSE, 'Debt-to-income ratio too high');
