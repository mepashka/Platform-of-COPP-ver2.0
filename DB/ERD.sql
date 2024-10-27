CREATE TABLE `Users` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR,
  `email` VARCHAR,
  `password` VARCHAR,
  `role` VARCHAR,
  `status` VARCHAR,
  `created_at` DATETIME
);

CREATE TABLE `Roles` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR,
  `description` TEXT,
  `email` VARCHAR,
  `registration_address` VARCHAR,
  `phone` VARCHAR
);

CREATE TABLE `UserRoles` (
  `user_id` INT,
  `role_id` INT
);

CREATE TABLE `AuthTokens` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `user_id` INT,
  `token` VARCHAR,
  `expires_at` DATETIME
);

CREATE TABLE `PasswordResets` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `user_id` INT,
  `token` VARCHAR,
  `expires_at` DATETIME
);

CREATE TABLE `UserProfiles` (
  `user_id` INT PRIMARY KEY,
  `photo` BLOB,
  `birth_date` DATE,
  `status` VARCHAR
);

CREATE TABLE `Organizations` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR,
  `address` VARCHAR,
  `phone` VARCHAR,
  `type` VARCHAR,
  `role` VARCHAR,
  `status` VARCHAR,
  `inn` VARCHAR,
  `ogrn` VARCHAR,
  `created_at` DATETIME
);

CREATE TABLE `Employers` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR,
  `contacts` VARCHAR,
  `industry` VARCHAR,
  `status` VARCHAR
);

CREATE TABLE `Customers` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR,
  `contacts` VARCHAR,
  `role` VARCHAR
);

CREATE TABLE `UserOrganizations` (
  `user_id` INT,
  `organization_id` INT,
  `role` VARCHAR
);

CREATE TABLE `Programs` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR,
  `description` TEXT,
  `organization_id` INT,
  `status` VARCHAR,
  `duration` INT,
  `cost` DECIMAL,
  `learning_format` VARCHAR,
  `category` VARCHAR
);

CREATE TABLE `Competencies` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR,
  `description` TEXT,
  `block` VARCHAR,
  `status` VARCHAR
);

CREATE TABLE `ProgramCompetencies` (
  `program_id` INT,
  `competency_id` INT
);

CREATE TABLE `Modules` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `program_id` INT,
  `name` VARCHAR,
  `description` TEXT,
  `competency_id` INT,
  `workload` INT
);

CREATE TABLE `Professions` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `industry` VARCHAR,
  `name` VARCHAR,
  `work_type` VARCHAR,
  `requirements` TEXT,
  `salary_level` VARCHAR,
  `restrictions` TEXT
);

CREATE TABLE `Feedback` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `program_id` INT,
  `user_id` INT,
  `rating` INT,
  `comment` TEXT
);

CREATE TABLE `FeedbackCategories` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR,
  `description` TEXT
);

CREATE TABLE `CareerGuidance` (
  `user_id` INT,
  `results` JSON
);

CREATE TABLE `Notifications` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `type` VARCHAR,
  `content` TEXT,
  `created_at` DATETIME
);

CREATE TABLE `ActivityLogs` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `user_id` INT,
  `action` TEXT,
  `created_at` DATETIME
);

CREATE TABLE `ProgramRecommendations` (
  `user_id` INT,
  `program_id` INT,
  `created_at` DATETIME
);

CREATE TABLE `ESIAIntegrationLogs` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `user_id` INT,
  `status` VARCHAR,
  `created_at` DATETIME
);

ALTER TABLE `UserRoles` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`);

ALTER TABLE `UserRoles` ADD FOREIGN KEY (`role_id`) REFERENCES `Roles` (`id`);

ALTER TABLE `AuthTokens` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`);

ALTER TABLE `PasswordResets` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`);

ALTER TABLE `UserProfiles` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`);

ALTER TABLE `UserOrganizations` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`);

ALTER TABLE `UserOrganizations` ADD FOREIGN KEY (`organization_id`) REFERENCES `Organizations` (`id`);

ALTER TABLE `Programs` ADD FOREIGN KEY (`organization_id`) REFERENCES `Organizations` (`id`);

ALTER TABLE `ProgramCompetencies` ADD FOREIGN KEY (`program_id`) REFERENCES `Programs` (`id`);

ALTER TABLE `ProgramCompetencies` ADD FOREIGN KEY (`competency_id`) REFERENCES `Competencies` (`id`);

ALTER TABLE `Modules` ADD FOREIGN KEY (`program_id`) REFERENCES `Programs` (`id`);

ALTER TABLE `Modules` ADD FOREIGN KEY (`competency_id`) REFERENCES `Competencies` (`id`);

ALTER TABLE `Feedback` ADD FOREIGN KEY (`program_id`) REFERENCES `Programs` (`id`);

ALTER TABLE `Feedback` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`);

ALTER TABLE `CareerGuidance` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`);

ALTER TABLE `ActivityLogs` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`);

ALTER TABLE `ProgramRecommendations` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`);

ALTER TABLE `ProgramRecommendations` ADD FOREIGN KEY (`program_id`) REFERENCES `Programs` (`id`);

ALTER TABLE `ESIAIntegrationLogs` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`);
