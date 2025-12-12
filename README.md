![](https://i.imgur.com/jMEypHm.png)

# Likeminds

> A website dedicated to creating and organizing STEM-focused book clubs, designed to promote collaborative learning, discussion, and knowledge sharing.

You can access the site [here](https://likeminds-0e01746d78a8.herokuapp.com/)

## Table of Contents

-  [Project Overview](#project-overview)
-  [User Experience (UX)](#user-experience-ux)
   -  [User Stories](#user-stories)
      -  [Must-Have Features (Implemented)](#must-have-features-implemented)
      -  [Could-Have Features (Backlog)](#could-have-features-backlog)
-  [Early Wireframes](#early-wireframes)
-  [Features](#features)
   -  [Landing page](#landing-page)
   -  [Book Clubs](#book-clubs)
   -  [Newsletter System](#newsletter-system)
   -  [Navigation & User Experience](#navigation--user-experience)
   -  [Design Philosophy](#design-philosophy)
   -  [Accessibility Features](#accessibility-features)
-  [Testing](#testing)
-  [Known Bugs](#known-bugs)
-  [Future Enhancements](#future-enhancements)
-  [Technologies Used](#technologies-used)
-  [Deployment](#deployment)

## Project Overview

Likeminds is a platform for learners, educators, and enthusiasts to form book clubs around STEM subjects.  
The goal is to make learning collaborative and engaging by combining structured reading with interactive events like puzzles, challenges, and community spotlights.

## User Experience (UX)

### User Stories

#### Must-Have Features (Implemented)

1. **Contact Details**

   -  As a user, I want to easily find contact information so that I can reach out for support or inquiries
   -  As a user, I want multiple ways to contact the platform (email, phone, address) for accessibility
   -  Acceptance Criteria: Contact section visible in footer on all pages with email, phone, and physical address

2. **About Page**

   -  As a new visitor, I want to understand what Likeminds is about so that I can determine if it meets my needs
   -  As a STEM enthusiast, I want to know the platform's mission and values to see if it aligns with my goals
   -  Acceptance Criteria: Dedicated about section explaining platform purpose, target audience, and benefits with supporting research

3. **Responsive Sizing**

   -  As a mobile user, I want the website to work perfectly on my device so that I can browse clubs on-the-go
   -  As a user with different screen sizes, I want consistent functionality across all devices
   -  Acceptance Criteria: Bootstrap responsive design working on mobile, tablet, and desktop with proper navigation collapse

4. **FAQ Page**

   -  As a new user, I want answers to common questions so that I can quickly understand how to use the platform
   -  As a club organizer, I want guidance on best practices so that my club will be successful
   -  Acceptance Criteria: Comprehensive FAQ section with accordion layout covering club creation, costs, management tips, and troubleshooting

5. **Club Viewing**

   -  As a STEM learner, I want to browse available clubs so that I can find ones that match my interests and schedule
   -  As a user, I want to filter clubs by subject and difficulty level so that I can find the most relevant options
   -  Acceptance Criteria: Clubs page with search functionality, subject filters, level filters, and paginated results showing club details

6. **Club Creation**

   -  As an educator/enthusiast, I want to create my own club so that I can lead discussions on topics I'm passionate about
   -  As a club organizer, I want to specify all relevant details so that potential members know exactly what to expect
   -  Acceptance Criteria: Multi-section form covering basic info, book/resources, schedule, settings, and organizer details with validation

7. **Signing Up**

   -  As a potential user, I want to sign up so I can access the rest of the site
   -  Acceptance Criteria: A working signup page with Django allauth integration
      ![](https://i.imgur.com/jtgacQi.png)

8. **Error Page**
   -  As a user who encounters a broken link, I want helpful guidance so that I can continue using the site
   -  As a visitor, I want error pages that maintain the site's design so that I feel confident in the platform's quality
   -  Acceptance Criteria: Custom 404 page with helpful suggestions, navigation options, and consistent branding

#### Could-Have Features (Backlog)

9. **Images and Branding**

   - As a user, I want visually appealing graphics and consistent branding so that the platform feels professional and trustworthy
   - As a visual learner, I want icons and images to help me quickly understand different sections and features

10. **Events Section**
    - As a community member, I want to participate in platform-wide events so that I can engage with the broader STEM learning community
    - As a club member, I want to see upcoming deadlines and special activities so that I can plan my participation

---

## Early Wireframes

As the project was coded and developed, the actual site changed a lot compared to the wireframe sketches, especially on the landing page.

-  Mobile view
   ![](https://i.imgur.com/NytSaVb.png)

![](https://i.imgur.com/l0j4UlZ.png)

-  Desktop view

![](https://i.imgur.com/y3GGAlX.png)

![](https://i.imgur.com/fXcdKVz.png)

Some choices were kept like the expanding line along the hero title, however this was too buggy on mobile, and so was only kept for larger screens.

As Django was introduced into the project, some pages had to be made. I wireframed the Club details page using Figma Make:

![](https://i.imgur.com/k0nta9B.png)

## Features

### Landing page

Introduces Likeminds, its purpose, and highlights the platform's mission of connecting STEM enthusiasts. Features a clean, Bootstrap-powered design with intuitive navigation, hero section with call-to-action buttons, and a comprehensive features showcase using modern card layouts.

### Book Clubs

-  **Create**: Comprehensive club creation form with sections for basic information, book/resource details, scheduling, club settings, and organizer information
-  **Browse**: Search and filter functionality allowing users to find clubs by subject (Physics, Mathematics, Programming, Engineering, Biology, Chemistry) and difficulty level (Beginner to Graduate)
-  **Details**: Each club displays member count, meeting times, difficulty level, and detailed descriptions
-  **Customization**: Club organizers can set privacy levels, approval requirements, prerequisites, and member expectations

### Newsletter System

-  **Signup Integration**: Newsletter modal accessible from footer on all pages
-  **Launch Notifications**: Dedicated signup page for early access notifications with interest-based preferences
-  **Privacy-Focused**: Clear consent mechanisms and unsubscribe options

### Navigation & User Experience

-  **Consistent Header**: Fixed navigation with active state indicators across all pages
-  **Smart Footer**: Comprehensive footer with quick links, contact information, and newsletter signup
-  **Error Handling**: Custom 404 page with helpful guidance and multiple pathways back to content

### Design Philosophy

-  **Clean Layout**: Focus on minimalism, prettiness and utility.
-  **Consistent Navigation**: Minimal navbar, with the feature to scroll back to it from the footer
-  **Color Scheme**:
   -  Primary brand color: `#2b2724` (dark brown/charcoal)
   -  Secondary color: `#37353b` (dark purple-gray)
   -  Highlight color: `#a0c9c0` (teal/mint green)
   -  Highlight light: `#dafffd` (very light teal)
   -  Background: `#fffef6` (warm white)
-  **Typography**:
   -  Heading font: `"cmu", sans-serif` - Computer Modern font family, widely recognized in STEM academia (especially TeX/LaTeX documents)
   -  Body font: `"Source Sans 3", sans-serif` - Clean, readable Source Sans 3 to promote the websites friendliness towards new learners.
   -  Fallback fonts: `"Fira Sans"` and system sans-serif stack
   -  Font size: Base 1.2rem for enhanced readability
   -  Clear spacing and hierarchy for readability.

### Accessibility Features

-  Semantic HTML for screen readers.
-  Minimal clutter and layout, with an accessible main content font.
-  Simple transitions, avoiding overstimulation.
-  High contrast text/backgrounds for accessibility.

---

## Testing

**Manual Testing**

-  **Responsive Design**: Verified Bootstrap grid system works correctly across mobile (320px+), tablet (768px+), and desktop (1200px+) viewports
-  **Navigation**: Tested all navigation links, active states, and mobile hamburger menu functionality - no dead links found
-  **Forms**: Validated club creation form, newsletter signup, and launch notification signup with proper validation and user feedback
-  **Interactive Elements**: Confirmed pagination styling, search/filter functionality, and modal operations work as expected
-  **Cross-Page Consistency**: Verified consistent header, footer, and styling across all pages (index, clubs, create, signup, error)

**Browser Testing**

-  **Firefox**: Full functionality
-  **Helium**: Works as expected, but may have unknown bugs as the browser is quite new
-  **Chrome**: Unsure, but since Helium is Chromium-based and in Alpha, it should also work
-  **Safari**: Unsure, but let me know!

**Validators**

-  **W3C HTML**: No issues
-  **W3C CSS**: Validation pending - custom stylesheet and Bootstrap overrides to be verified
-  **WCAG Accessibility**: 87%
-  **Lighthouse report**: ![](https://i.imgur.com/9U4hRoF.png)

---

## Future Enhancements

-  **Site load**: Optimize font loading and external platform requests for better performance and load times
-  **Accessibility**: Increase aria labelling of site content for those who are visually impaired
-  **Calendar Integration**: Sync club meeting schedules with popular calendar applications
-  **Progress Tracking**: Reading progress indicators and milestone achievements

## Technologies Used

-  **Frontend**: HTML5, CSS3, JavaScript (ES6+), Django, Python 3.12.10
-  **Framework**: Bootstrap 5.3.8 for responsive design and components
-  **Icons**: FontAwesome 6.4.0 for consistent iconography
-  **Fonts**: Google Fonts (Source Sans 3, Computer Modern) with Fira Sans and Sans-Serif fallbacks
-  **Version Control**: Git with GitHub repository hosting
-  **Development**: VS Code with live server for local development, Neovim version 0.11.2

## Django Implementation

The dynamic portion of Likeminds uses Django to power club listings, detail pages, and user actions. Key elements:

-  **Models**: A `Club` model captures organizer info, privacy settings (`is_private`, `require_approval`), membership lists (`approved_members`, `unapproved_members`), and rich content fields (briefing, prerequisites, expectations, schedule).
-  **Forms**: A `ClubForm` ModelForm provides a unified editing experience and renders with Crispy Forms (Bootstrap 5 template pack) inside a modal for owners.
-  **Views**:
   -  `ClubList` (class-based): Lists public clubs, annotated with `approved_count` for quick display.
   -  `club_detail`: Shows a single club; if the viewer is the owner, includes the edit form/modal.
   -  `club_create`: Handles new club creation; automatically adds the creator as an approved member.
   -  `club_join`: Adds users to `approved_members` or `unapproved_members` depending on `require_approval`.
   -  `club_update`: Owner-only inline edits via the modal; returns messages on success/error.
   -  `my_clubs`: Aggregates “Created”, “Joined”, and “Pending” clubs for the signed-in user.
   -  `club_delete`: Owner-only deletion with a typed confirmation gate (“I understand”), then redirect to `my_clubs`.
-  **URLs**: Routes include `clubs/`, `create/`, `my-clubs/`, `join/<slug>/`, `update/<slug>/`, `delete/<slug>/`, and `/<slug>/` for details.
-  **Templates**: Django template inheritance via `base.html`; Bootstrap-styled components throughout (`club_detail.html`, `my_clubs.html`). Navbar shows “My Clubs” only for authenticated users.
-  **Messages**: Django messages surface feedback for join/update/delete; site renders them as styled overlay alerts.

## CRUD Features

Likeminds implements full CRUD around clubs, with permissions and safe-guards:

-  **Create**:

   -  Path: `club_create` (`/clubs/create/`)
   -  Form: `ClubForm` with validation and Bootstrap/Crispy styling.
   -  Behavior: Sets `author` and adds the creator to `approved_members`; redirects to club listings.

-  **Read**:

   -  Paths: `ClubList` (`/clubs/`) for browsing; `club_detail` (`/clubs/<slug>/`) for details.
   -  Details page: Displays organizer info, privacy/approval badges, membership count, schedule, expectations, and prerequisites.

-  **Update**:

   -  Path: `club_update` (`/clubs/update/<slug>/`)
   -  Access: Owner-only; triggered from “Edit Details” button in club detail.
   -  UX: Modal with Crispy-rendered `ClubForm`; success/error messages provided.

-  **Delete**:

   -  Path: `club_delete` (`/clubs/delete/<slug>/`)
   -  Access: Owner-only; requires entering the phrase “I understand” in a confirmation modal.
   -  Behavior: Deletes the club and redirects user to `my_clubs` with a success message.

-  **Join/Approval Flow**:
   -  Path: `club_join` (`/clubs/join/<slug>/`)
   -  Logic: If `require_approval` is true, the user is added to `unapproved_members` and sees a “Request sent” message. Otherwise, they are added to `approved_members` and see a success message.
   -  Duplicates: If already approved or pending, informative messages are shown without changing membership.

These features are wired with Django’s authentication checks, Bootstrap-styled templates, and clean URL routing to provide a cohesive, user-friendly experience.

## Deployment

-  **Platform**: Heroku
-  **CDN**: Bootstrap and FontAwesome served via CDN for optimal performance

---

## Getting Started (Django)

Run the dynamic Django app locally:

1. Prerequisites

   -  Python 3.10+
   -  Virtual environment tool (`venv` or `conda`)

2. Setup

```powershell
# From the project root
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
# This installs the exact versions pinned in the project’s requirements.txt
# including Django, django-crispy-forms, and crispy-bootstrap5
```

3. Configure

   -  In `settings.py`:
      -  Add `crispy_forms` and `crispy_bootstrap5` to `INSTALLED_APPS`.
      -  Set `CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"` and `CRISPY_TEMPLATE_PACK = "bootstrap5"`.
   -  Ensure static files are served from `static/` so `static/css/style.css` loads.

4. Run

```powershell
python manage.py migrate
python manage.py runserver
```

5. Create superuser (optional, recommended for testing owner features)

```powershell
python manage.py createsuperuser
```

6. Navigate

   -  `/clubs/` — browse public clubs
   -  `/clubs/create/` — create a club
   -  `/clubs/my-clubs/` — view created, joined, and pending clubs

7. Static files (if needed)
   -  Ensure `STATIC_URL` is configured; during local dev Django serves files automatically.
   -  If using `collectstatic` for deployment:

```powershell
python manage.py collectstatic --noinput
```
