-- 1. Show all denied loans
SELECT * FROM loans WHERE denial_reason IS NOT NULL;
-- 2. Calculate average loan value
SELECT AVG(loan_value) AS average_loan_value FROM loans;
-- 3. Show income and denial reason for non-owner-occupied properties
SELECT applicant_income, denial_reason FROM loans WHERE owner_occupied = FALSE;
