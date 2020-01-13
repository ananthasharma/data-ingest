CREATE TABLE `capm`.`role_master` (
  `role_id` INT NOT NULL AUTO_INCREMENT,
  `role_name` VARCHAR(45) NULL,
  `status` VARCHAR(1) NULL,
  PRIMARY KEY (`role_id`));

CREATE TABLE `capm`.`user_master` (
  `user_id` VARCHAR(7) NOT NULL,
  `name` VARCHAR(45) NULL,
  `status` VARCHAR(1) NULL DEFAULT 'T',
  PRIMARY KEY (`user_id`));

CREATE TABLE `capm`.`user_role_assoc` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(7) NOT NULL,
  `role_id` INT NOT NULL,
  `mapping_id` INT NULL,
  `status` VARCHAR(1) NOT NULL DEFAULT 'T',
  PRIMARY KEY (`id`));

CREATE TABLE `capm`.`mapping_master` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ingest_date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
  `file_content_as_blob` BLOB NULL,
  `file_name` VARCHAR(200) NULL,
  PRIMARY KEY (`id`));

ALTER TABLE `capm`.`user_role_assoc`
ADD INDEX `URA_USER_FK_idx` (`user_id` ASC) VISIBLE,
ADD INDEX `URA_ROLE_FK_idx` (`role_id` ASC) VISIBLE,
ADD INDEX `URA_MAPPING_FK_idx` (`mapping_id` ASC) VISIBLE;
;
ALTER TABLE `capm`.`user_role_assoc`
ADD CONSTRAINT `URA_USER_FK`
  FOREIGN KEY (`user_id`)
  REFERENCES `capm`.`user_master` (`user_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `URA_ROLE_FK`
  FOREIGN KEY (`role_id`)
  REFERENCES `capm`.`role_master` (`role_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `URA_MAPPING_FK`
  FOREIGN KEY (`mapping_id`)
  REFERENCES `capm`.`mapping_master` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


ALTER TABLE `capm`.`user_master`
ADD COLUMN `mapping_id` INT NULL AFTER `status`,
ADD INDEX `USER_MAPPING_FK_idx` (`mapping_id` ASC) VISIBLE;
;
ALTER TABLE `capm`.`user_master`
ADD CONSTRAINT `USER_MAPPING_FK`
  FOREIGN KEY (`mapping_id`)
  REFERENCES `capm`.`mapping_master` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


ALTER TABLE `capm`.`role_master`
ADD COLUMN `mapping_id` INT NULL AFTER `status`,
ADD INDEX `ROLE_MAPPING_FK_idx` (`mapping_id` ASC) VISIBLE;
;
ALTER TABLE `capm`.`role_master`
ADD CONSTRAINT `ROLE_MAPPING_FK`
  FOREIGN KEY (`mapping_id`)
  REFERENCES `capm`.`mapping_master` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
