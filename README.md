
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
- **Attributes**: First name, Last name, Email, Password, Admin status.
- **Operations**: Register, update profile, delete account.
Example:
- **First Name**: A string representing the user’s first name.
- **Last Name**: A string representing the user’s last name.
- **Email**: A unique identifier for each user.
- **Password**: Used for authentication, stored securely (hashed).
- **Admin Status**: Boolean flag to determine if a user is an admin.
### Place Entity
- **Attributes**: Title, description, price, latitude, longitude, owner, list of amenities.
Example:
- **Title**: A string representing the place's title (e.g., "Cozy Apartment").
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

![HBnB---UML_High-Level-Package-Diagram](https://github.com/user-attachments/assets/4f400db1-537b-49e7-811f-f50bc68f3605)

## Detailed Class Diagram for Business Logic Layer
The class diagram for the Business Logic Layer consists of four main entities:  **User**, **Place**, **Review**, and **Amenity**. 

![HBnB---UML](https://github.com/user-attachments/assets/e1a66de0-02e9-497f-a798-87d32d14077e)

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
Name: [Flavio Avdulla](https://github.com/FlavioAvdulla)

Name: [Stilian Saka](https://github.com/StilianSaka)

Name: [Hans Sora](https://github.com/HansSora)

Name: [Gerti Bajo](https://github.com/Gerti23)
