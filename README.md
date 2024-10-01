
# Air BnB Clone - Technical Documentation

## Context and Objective
In this phase, we are focusing on documenting the technical architecture of the HBnB Evolution application. This documentation serves to provide a clear understanding of the system's structure, interactions, and design decisions. The HBnB Evolution application will enable users to manage places, reviews, and amenities. This document provides visual representations using UML diagrams to describe the overall architecture and interactions between the layers.
## Problem Description
**HBnB Evolution is a simplified AirBnB-like application with the following main operations**:
- **User Management**: Users can register, log in, and manage their profiles.
- **Place Management**: Owners can create, update, and list their properties (places) with details like title, description, and amenities.
- **Review Management**: Users can leave reviews and ratings for places they have visited.
- **Amenity Management**: Amenities such as Wi-Fi or parking can be added to places.
The application follows a layered architecture to separate the responsibilities between the presentation, business logic, and persistence layers.
## Business Rules and Requirements


### User Entity
- Each user has a first name, last name, email, and password.
- Users can be identified as administrators through a boolean attribute.
- Users should be able to register, update their profile information, and be deleted.

### Place Entity
- Each place has a title, description, price, latitude, and longitude.
- Places are associated with the user who created them (owner).
- Places can have a list of amenities.
- Places can be created, updated, deleted, and listed.

### Review Entity
- Each review is associated with a specific place and user, and includes a rating and comment.
- Reviews can be created, updated, deleted, and listed by place.

### Amenity Entity
- Each amenity has a name, and description.
- Amenities can be created, updated, deleted, and listed.
 "Cozy Apartment").
- **Price**: A float value representing the cost per night.
- **Latitude/Longitude**: Coordinates used to map the place's location.

## UML Documentation and Diagrams
### High-Level Package Diagram
**The HBnB Evolution application follows a three-layered architecture**:
- **Presentation Layer**: The user interacts with the system via APIs.
- functionality such as user registration, place creation, and review management.
- **Persistence Layer**: Responsible for storing and retrieving data from the database.
The Facade pattern is used to communicate between layers, ensuring a clean separation of concerns.
In the high-level package diagram, we depict the three main layers of the HBnB Evolution project: Presentation Layer, Business Logic Layer, and Persistence Layer. The facade pattern is used to handle communication between these layers.
- **Presentation Layer**: Handles API calls and user interactions.
- **Business Logic Layer**: Includes the core business logic and models.
- **Persistence Layer**: Manages data storage.

![HBnB---UML_High-Level-Package-Diagram](https://github.com/user-attachments/assets/e82d28b2-5a1a-4fac-a680-7c8fd855e944)

### Detailed Class Diagram for Business Logic Layer
The class diagram for the Business Logic Layer consists of four main entities:  **User**, **Place**, **Review**, and **Amenity**. 

![HBnB - UML](https://github.com/user-attachments/assets/6ee8375a-96d3-4c8b-ad09-f8757f4e08c7)

### High-Level Squence diagram

### **User Registration**: A user signs up for a new account.
![registration](https://github.com/user-attachments/assets/c3d4c558-ca05-4164-a359-8a7e157dd7e0)
### **Place Creation**: A user creates a new place listing.
![create-place](https://github.com/user-attachments/assets/583a6e1e-9f83-455d-948d-625910f1275e)
### **Review Submission**: A user submits a review for a place.
![review](https://github.com/user-attachments/assets/529f86d3-99a5-4a62-8323-48fd45c62ca5)
### **Fetching a List of Places**: A user requests a list of places based on certain criteria.
![list-of-places](https://github.com/user-attachments/assets/064425f2-4e88-403c-b12a-3cd8d184d492)

## Entities
### User

The User class includes attributes like first name, last name, email, password, and an `is_admin` flag to distinguish administrators from regular users. The key methods for this class are `register()`, `update_profile()`, and `delete_account()`, which allow users to manage their accounts. 
Relationships
- A User can own multiple Places.
- A Place can have multiple Amenities and multiple Reviews.
- A Review is associated with a User and a Place.

### Review

Description: The Review class represents a review that a user can leave for a place. It includes attributes like user (a User object), place (a Place object), rating, and comment. The key methods for this class are update_review() and delete_review(), which allow for updating and deleting reviews.
- A Review is associated with a User and a Place.

### Place

Description: The Place class represents a place that can be owned by a user. It includes attributes like name, location, owner (a User object), amenities (a list of Amenity objects), and reviews (a list of Review objects). The key methods for this class are add_amenity(), add_review(), update_place(), and delete_place(), which allow for managing the place and its associated amenities and reviews.
- A User can own multiple Places.
- A Place can have multiple Amenities and multiple Reviews.

### Amenity

Description: The Amenity class represents an amenity that can be associated with a place. It includes attributes like name and description. The key methods for this class are update_amenity() and delete_amenity(), which allow for updating and deleting amenities.

## Collaborators
- [Flavio Avdulla](https://github.com/FlavioAvdulla)

- [Stilian Saka](https://github.com/StilianSaka)

- [Hans Sora](https://github.com/HansSora)

- [Gerti Bajo](https://github.com/Gerti23)
