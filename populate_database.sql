SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- Insert user data (20 visitors, 5 helpers, 2 admins)
INSERT INTO users (user_name, password_hash, email, first_name, last_name, location, profile_image, role, status)
VALUES 
('visitor1', 'hash1', 'visitor1@example.com', 'John', 'Doe', 'New York', '', 'visitor', 'active'),
('visitor2', 'hash2', 'visitor2@example.com', 'Jane', 'Smith', 'Los Angeles', '', 'visitor', 'active'),
('visitor3', 'hash3', 'visitor3@example.com', 'Tom', 'Brown', 'Chicago', '', 'visitor', 'active'),
('visitor4', 'hash4', 'visitor4@example.com', 'Alice', 'Johnson', 'Houston', '', 'visitor', 'active'),
('visitor5', 'hash5', 'visitor5@example.com', 'Bob', 'Williams', 'Miami', '', 'visitor', 'active'),
('visitor6', 'hash6', 'visitor6@example.com', 'Charlie', 'Davis', 'Seattle', '', 'visitor', 'active'),
('visitor7', 'hash7', 'visitor7@example.com', 'Diana', 'Moore', 'Denver', '', 'visitor', 'active'),
('visitor8', 'hash8', 'visitor8@example.com', 'Ethan', 'Taylor', 'San Francisco', '', 'visitor', 'active'),
('visitor9', 'hash9', 'visitor9@example.com', 'Frank', 'Anderson', 'Boston', '', 'visitor', 'active'),
('visitor10', 'hash10', 'visitor10@example.com', 'Grace', 'Thomas', 'Atlanta', '', 'visitor', 'active'),
('visitor11', 'hash11', 'visitor11@example.com', 'Harry', 'Harris', 'Dallas', '', 'visitor', 'active'),
('visitor12', 'hash12', 'visitor12@example.com', 'Ivy', 'Clark', 'San Diego', '', 'visitor', 'active'),
('visitor13', 'hash13', 'visitor13@example.com', 'Jack', 'Lewis', 'Phoenix', '', 'visitor', 'active'),
('visitor14', 'hash14', 'visitor14@example.com', 'Kate', 'Walker', 'Portland', '', 'visitor', 'active'),
('visitor15', 'hash15', 'visitor15@example.com', 'Leo', 'Hall', 'Las Vegas', '', 'visitor', 'active'),
('visitor16', 'hash16', 'visitor16@example.com', 'Mia', 'Allen', 'Nashville', '', 'visitor', 'active'),
('visitor17', 'hash17', 'visitor17@example.com', 'Nathan', 'Young', 'Philadelphia', '', 'visitor', 'active'),
('visitor18', 'hash18', 'visitor18@example.com', 'Olivia', 'King', 'Orlando', '', 'visitor', 'active'),
('visitor19', 'hash19', 'visitor19@example.com', 'Paul', 'Wright', 'Detroit', '', 'visitor', 'active'),
('visitor20', 'hash20', 'visitor20@example.com', 'Quinn', 'Scott', 'Minneapolis', '', 'visitor', 'active'),

('helper1', 'hash21', 'helper1@example.com', 'Ron', 'Adams', 'Austin', '', 'helper', 'active'),
('helper2', 'hash22', 'helper2@example.com', 'Sophia', 'Nelson', 'Charlotte', '', 'helper', 'active'),
('helper3', 'hash23', 'helper3@example.com', 'Travis', 'Hill', 'Columbus', '', 'helper', 'active'),
('helper4', 'hash24', 'helper4@example.com', 'Uma', 'Green', 'Indianapolis', '', 'helper', 'active'),
('helper5', 'hash25', 'helper5@example.com', 'Victor', 'Baker', 'San Jose', '', 'helper', 'active'),

('admin1', 'hash26', 'admin1@example.com', 'Walter', 'Gonzalez', 'Washington', '', 'admin', 'active'),
('admin2', 'hash27', 'admin2@example.com', 'Xena', 'Carter', 'St. Louis', '', 'admin', 'active');

-- Insert `issue` data（at least 20 issues）
INSERT INTO issues (user_id, summary, description, status)
VALUES 
(1, 'Issue 1', 'Description for issue 1', 'new'),
(2, 'Issue 2', 'Description for issue 2', 'open'),
(3, 'Issue 3', 'Description for issue 3', 'stalled'),
(4, 'Issue 4', 'Description for issue 4', 'resolved'),
(5, 'Issue 5', 'Description for issue 5', 'new'),
(6, 'Issue 6', 'Description for issue 6', 'open'),
(7, 'Issue 7', 'Description for issue 7', 'stalled'),
(8, 'Issue 8', 'Description for issue 8', 'resolved'),
(9, 'Issue 9', 'Description for issue 9', 'new'),
(10, 'Issue 10', 'Description for issue 10', 'open'),
(11, 'Issue 11', 'Description for issue 11', 'stalled'),
(12, 'Issue 12', 'Description for issue 12', 'resolved'),
(13, 'Issue 13', 'Description for issue 13', 'new'),
(14, 'Issue 14', 'Description for issue 14', 'open'),
(15, 'Issue 15', 'Description for issue 15', 'stalled'),
(16, 'Issue 16', 'Description for issue 16', 'resolved'),
(17, 'Issue 17', 'Description for issue 17', 'new'),
(18, 'Issue 18', 'Description for issue 18', 'open'),
(19, 'Issue 19', 'Description for issue 19', 'stalled'),
(20, 'Issue 20', 'Description for issue 20', 'resolved');

-- Insert `comments` data（at least 20，some issues contain multiple comments，some contains nothing）
INSERT INTO comments (issue_id, user_id, content)
VALUES 
(1, 2, 'Comment 1 on issue 1'),
(1, 3, 'Comment 2 on issue 1'),
(2, 4, 'Comment on issue 2'),
(3, 5, 'Comment on issue 3'),
(4, 6, 'Comment on issue 4'),
(5, 7, 'Comment 1 on issue 5'),
(5, 8, 'Comment 2 on issue 5'),
(6, 9, 'Comment on issue 6'),
(7, 10, 'Comment on issue 7'),
(8, 11, 'Comment on issue 8'),
(9, 12, 'Comment on issue 9'),
(10, 13, 'Comment on issue 10'),
(11, 14, 'Comment on issue 11'),
(12, 15, 'Comment 1 on issue 12'),
(12, 16, 'Comment 2 on issue 12'),
(13, 17, 'Comment on issue 13'),
(14, 18, 'Comment on issue 14'),
(15, 19, 'Comment on issue 15'),
(16, 20, 'Comment on issue 16'),
(17, 1, 'Comment on issue 17');

SET FOREIGN_KEY_CHECKS = 1;