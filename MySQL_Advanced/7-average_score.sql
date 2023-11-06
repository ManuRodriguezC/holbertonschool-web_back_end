-- Creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
 DECLARE total_score INT;
 DECLARE num_scores INT;
 DECLARE avg_score FLOAT;

 SELECT SUM(score), COUNT(score) INTO total_score, num_scores FROM corrections WHERE user_id = user_id;

 SET avg_score = total_score / num_scores;

 UPDATE users SET average_score = avg_score WHERE id = user_id;
END; //
DELIMITER ;
