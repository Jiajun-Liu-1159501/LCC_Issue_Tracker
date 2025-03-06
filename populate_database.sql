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

-- Insert issue data (at least 20 issues with more realistic summaries and descriptions)
INSERT INTO issues (user_id, summary, description, status)
VALUES 
(1, 'Website is down', 'The main website is not loading, causing users to be unable to access the platform.', 'new'),
(2, 'Login error', 'Users are unable to log in using their credentials, resulting in failed login attempts.', 'open'),
(3, 'Broken link on homepage', 'The contact us page link is broken and leads to a 404 error.', 'resolved'),
(4, 'Slow website performance', 'The website is taking too long to load, leading to user frustration and potential loss of traffic.', 'open'),
(5, 'Mobile view issues', 'The website does not render properly on mobile devices, making it difficult for users to navigate.', 'new'),
(6, 'Search bar not working', 'The search functionality does not return results even for known queries.', 'stalled'),
(7, 'Payment gateway error', 'Users are facing errors when attempting to make payments, preventing them from completing purchases.', 'open'),
(8, 'Broken images on product pages', 'Images for several products are not loading, making the pages look incomplete.', 'resolved'),
(9, 'Account password reset issue', 'Users who request a password reset do not receive the reset email, preventing account recovery.', 'new'),
(10, 'Form validation error', 'Form submissions are failing due to incorrect or missing validation on required fields.', 'open'),
(11, 'Missing order confirmation emails', 'Customers who complete a purchase are not receiving order confirmation emails.', 'resolved'),
(12, 'Coupon codes not applying', 'Promo codes are not applying at checkout, even though they are valid.', 'new'),
(13, 'Broken authentication flow', 'The two-factor authentication step does not work, causing login issues for some users.', 'open'),
(14, 'Dashboard display issue', 'The admin dashboard displays incorrect user data and does not update in real time.', 'stalled'),
(15, 'API response error', 'The API is returning invalid responses for certain endpoints, causing data to be displayed incorrectly.', 'resolved'),
(16, 'Error in product filtering', 'The product filter on the shop page does not show relevant results when used.', 'new'),
(17, 'Incorrect order status', 'Some customers are seeing incorrect order statuses in their order history.', 'open'),
(18, 'Outdated content on FAQ page', 'The FAQ page contains outdated information that needs to be updated to reflect current policies.', 'resolved'),
(19, 'Error while uploading files', 'File upload functionality is broken, and users cannot upload documents or images to the platform.', 'new'),
(20, 'Localization issue', 'The website is not displaying content in the correct language based on the user’s region settings.', 'open');

-- Insert comment data (at least 20, some issues with multiple comments)
INSERT INTO comments (issue_id, user_id, content)
VALUES 
(1, 2, 'Reported issue with the website being down, needs urgent attention.'),
(1, 3, 'Agreed, the website being down is a major problem.'),
(2, 4, 'Can’t log in after several attempts, please prioritize this fix.'),
(3, 5, 'The broken link issue has been fixed, please confirm.'),
(4, 6, 'The site speed is really slow for me, especially during peak hours.'),
(5, 7, 'Mobile view is a disaster. Hope this gets fixed soon!'),
(6, 8, 'Search bar issue persists, even after clearing the cache.'),
(7, 9, 'Payment gateway issue is affecting transactions, needs to be resolved.'),
(8, 10, 'Images have been fixed, everything looks good now!'),
(9, 11, 'I did not receive the password reset email, can you check again?'),
(10, 12, 'The form validation error occurs on the checkout page.'),
(11, 13, 'Order confirmation email hasn’t been received yet.'),
(12, 14, 'I’m trying to apply a coupon code but it’s not working at all.'),
(13, 15, 'Two-factor authentication step is broken on my account.'),
(14, 16, 'Dashboard display issue is very frustrating, can’t see any user stats.'),
(15, 17, 'API responses are delayed, making the user experience worse.'),
(16, 18, 'Filtering does not work on certain products, they keep showing in results.'),
(17, 19, 'The order status is completely wrong, it says shipped but it’s still processing.'),
(18, 1, 'The FAQ page needs updating as many questions are outdated.'),
(19, 2, 'File upload feature is broken, nothing works when trying to upload a document.'),
(20, 3, 'Localization issue persists, language settings aren’t saving on my account.');

SET FOREIGN_KEY_CHECKS = 1;