SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- Insert user data (20 visitors, 5 helpers, 2 admins)
INSERT INTO users (user_name, password_hash, email, first_name, last_name, location, profile_image, role, status)
VALUES 
('visitor1', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor1@example.com', 'John', 'Doe', 'New York', '', 'visitor', 'active'),
('visitor2', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor2@example.com', 'Jane', 'Smith', 'Los Angeles', '', 'visitor', 'active'),
('visitor3', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor3@example.com', 'Tom', 'Brown', 'Chicago', '', 'visitor', 'active'),
('visitor4', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor4@example.com', 'Alice', 'Johnson', 'Houston', '', 'visitor', 'active'),
('visitor5', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor5@example.com', 'Bob', 'Williams', 'Miami', '', 'visitor', 'active'),
('visitor6', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor6@example.com', 'Charlie', 'Davis', 'Seattle', '', 'visitor', 'active'),
('visitor7', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor7@example.com', 'Diana', 'Moore', 'Denver', '', 'visitor', 'active'),
('visitor8', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor8@example.com', 'Ethan', 'Taylor', 'San Francisco', '', 'visitor', 'active'),
('visitor9', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor9@example.com', 'Frank', 'Anderson', 'Boston', '', 'visitor', 'active'),
('visitor10', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor10@example.com', 'Grace', 'Thomas', 'Atlanta', '', 'visitor', 'active'),
('visitor11', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor11@example.com', 'Harry', 'Harris', 'Dallas', '', 'visitor', 'active'),
('visitor12', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor12@example.com', 'Ivy', 'Clark', 'San Diego', '', 'visitor', 'active'),
('visitor13', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor13@example.com', 'Jack', 'Lewis', 'Phoenix', '', 'visitor', 'active'),
('visitor14', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor14@example.com', 'Kate', 'Walker', 'Portland', '', 'visitor', 'active'),
('visitor15', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor15@example.com', 'Leo', 'Hall', 'Las Vegas', '', 'visitor', 'active'),
('visitor16', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor16@example.com', 'Mia', 'Allen', 'Nashville', '', 'visitor', 'active'),
('visitor17', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor17@example.com', 'Nathan', 'Young', 'Philadelphia', '', 'visitor', 'active'),
('visitor18', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor18@example.com', 'Olivia', 'King', 'Orlando', '', 'visitor', 'active'),
('visitor19', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor19@example.com', 'Paul', 'Wright', 'Detroit', '', 'visitor', 'active'),
('visitor20', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'visitor20@example.com', 'Quinn', 'Scott', 'Minneapolis', '', 'visitor', 'active'),

('helper1', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'helper1@example.com', 'Ron', 'Adams', 'Austin', '', 'helper', 'active'),
('helper2', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'helper2@example.com', 'Sophia', 'Nelson', 'Charlotte', '', 'helper', 'active'),
('helper3', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'helper3@example.com', 'Travis', 'Hill', 'Columbus', '', 'helper', 'active'),
('helper4', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'helper4@example.com', 'Uma', 'Green', 'Indianapolis', '', 'helper', 'active'),
('helper5', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'helper5@example.com', 'Victor', 'Baker', 'San Jose', '', 'helper', 'active'),

('admin1', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'admin1@example.com', 'Walter', 'Gonzalez', 'Washington', '', 'admin', 'active'),
('admin2', '$2b$12$9ox5GcobYTzD53.wVBbFpeHS1lPjqNWYpRM9C1RQGJlSnRJbPvrOe', 'admin2@example.com', 'Xena', 'Carter', 'St. Louis', '', 'admin', 'active');

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