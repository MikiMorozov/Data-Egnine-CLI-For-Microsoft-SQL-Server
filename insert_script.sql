Certainly! Here are the SQL Server insert statements for each table with 5 lines of dummy data:


-- Table: price_info
INSERT INTO price_info (adult_price, child_price, discount, adult_age)
VALUES (100, 50, 10, 18),
       (120, 60, 15, 16),
       (90, 40, 5, 20),
       (110, 55, 12, 17),
       (95, 45, 8, 19);

-- Table: description
INSERT INTO description (name, description, duration, location, activity_status)
VALUES ('Hiking Adventure', 'Explore the trails and enjoy the picturesque views.', 120, 'Mountain Peak', 1),
       ('Scuba Diving Experience', 'Discover the underwater world with professional instructors.', 180, 'Coral Reef', 1),
       ('Cycling Tour', 'Ride through scenic routes and visit historical landmarks.', 150, 'Countryside', 1),
       ('Skiing Trip', 'Hit the slopes and experience the thrill of winter sports.', 180, 'Mountain Resort', 1),
       ('Safari Adventure', 'Encounter exotic wildlife in their natural habitat.', 240, 'Savannah', 1);

-- Table: contact_info
INSERT INTO contact_info (phone, email, address)
VALUES ('123-456-7890', 'info@example.com', '123 Main Street, CityA'),
       ('456-789-0123', 'contactus@example.com', '456 Elm Street, CityB'),
       ('789-012-3456', 'support@example.com', '789 Oak Street, CityC'),
       ('321-654-9870', 'info@example.com', '321 Pine Street, CityD'),
       ('654-987-0123', 'admin@example.com', '654 Maple Street, CityE');

-- Table: organizer
INSERT INTO organizer (name, contact_info_id)
VALUES ('Adventure Excursions', 1),
       ('Underwater Expeditions', 2),
       ('Cycle Ventures', 3),
       ('Snowbound Escapades', 4),
       ('Wildlife Expeditions', 5);

-- Table: customer
INSERT INTO customer (name, contact_info_id, activity_status)
VALUES ('John Doe', 1, 1),
       ('Jane Smith', 2, 1),
       ('Michael Johnson', 3, 1),
       ('Emily Davis', 4, 1),
       ('Chris Wilson', 5, 1);

-- Table: activity
INSERT INTO activity (fixture, nr_of_places, price_info_id, description_id, organizer_id)
VALUES ('2023-05-15 10:00:00', 20, 1, 1, 1),
       ('2023-06-20 12:00:00', 15, 2, 2, 2),
       ('2023-07-10 09:00:00', 25, 3, 3, 3),
       ('2023-08-05 11:00:00', 18, 4, 4, 4),
       ('2023-09-30 08:30:00', 30, 5, 5, 5);

-- Table: registration
INSERT INTO registration (activity_id, customer_id, total_price)
VALUES (1, 1, 200),
       (2, 2, 300),
       (3, 3, 250),
       (4, 4, 350),
       (5, 5, 400);

-- Table: member
INSERT INTO member (name, birthday, customer_id, activity_status)
VALUES ('Alex Johnson', '2000-03-10', 1, 1),
       ('Olivia Brown', '1998-07-20', 2, 1),
       ('William Taylor', '2005-01-05', 3, 1),
       ('Sophia Clark', '2007-09-15', 4, 1),
       ('Daniel Martinez', '1995-11-30', 5, 1);

-- Table: registration_details
INSERT INTO registration_details (registration_id, member_id, subtotal_price)
VALUES (1, 1, 100),
       (2, 2, 150),
       (3, 3, 125),
       (4, 4, 175),
       (5, 5, 200);