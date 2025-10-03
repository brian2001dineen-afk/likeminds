# Likeminds

> A website dedicated to creating and organizing STEM-focused book clubs, designed to promote collaborative learning, discussion, and knowledge sharing.

---

## Project Overview

Likeminds is a platform for learners, educators, and enthusiasts to form book clubs around STEM subjects.  
The goal is to make learning collaborative and engaging by combining structured reading with interactive events like puzzles, challenges, and community spotlights.

---
`
## User Experience (UX)

### User Stories

#### Must-Have Features (Implemented)

1. **Contact Details**

    - As a user, I want to easily find contact information so that I can reach out for support or inquiries
    - As a user, I want multiple ways to contact the platform (email, phone, address) for accessibility
    - Acceptance Criteria: Contact section visible in footer on all pages with email, phone, and physical address

2. **About Page**

    - As a new visitor, I want to understand what Likeminds is about so that I can determine if it meets my needs
    - As a STEM enthusiast, I want to know the platform's mission and values to see if it aligns with my goals
    - Acceptance Criteria: Dedicated about section explaining platform purpose, target audience, and benefits with supporting research

3. **Responsive Sizing**

    - As a mobile user, I want the website to work perfectly on my device so that I can browse clubs on-the-go
    - As a user with different screen sizes, I want consistent functionality across all devices
    - Acceptance Criteria: Bootstrap responsive design working on mobile, tablet, and desktop with proper navigation collapse

4. **FAQ Page**

    - As a new user, I want answers to common questions so that I can quickly understand how to use the platform
    - As a club organizer, I want guidance on best practices so that my club will be successful
    - Acceptance Criteria: Comprehensive FAQ section with accordion layout covering club creation, costs, management tips, and troubleshooting

5. **Club Viewing**

    - As a STEM learner, I want to browse available clubs so that I can find ones that match my interests and schedule
    - As a user, I want to filter clubs by subject and difficulty level so that I can find the most relevant options
    - Acceptance Criteria: Clubs page with search functionality, subject filters, level filters, and paginated results showing club details

6. **Club Creation**

    - As an educator/enthusiast, I want to create my own club so that I can lead discussions on topics I'm passionate about
    - As a club organizer, I want to specify all relevant details so that potential members know exactly what to expect
    - Acceptance Criteria: Multi-section form covering basic info, book/resources, schedule, settings, and organizer details with validation

7. **Signing Up**

    - As a potential user, I want to sign up for launch notifications so that I can be among the first to join
    - As an interested learner, I want to specify my interests so that I receive relevant updates
    - Acceptance Criteria: Email signup form with optional interest selection, privacy agreements, and newsletter integration

8. **Error Page**
    - As a user who encounters a broken link, I want helpful guidance so that I can continue using the site
    - As a visitor, I want error pages that maintain the site's design so that I feel confident in the platform's quality
    - Acceptance Criteria: Custom 404 page with helpful suggestions, navigation options, and consistent branding

#### Could-Have Features (Backlog)

9. **Images and Branding**

    - As a user, I want visually appealing graphics and consistent branding so that the platform feels professional and trustworthy
    - As a visual learner, I want icons and images to help me quickly understand different sections and features

10. **Events Section**
    - As a community member, I want to participate in platform-wide events so that I can engage with the broader STEM learning community
    - As a club member, I want to see upcoming deadlines and special activities so that I can plan my participation

---

## Early Wireframes
![](https://i.imgur.com/NytSaVb.png)
![](https://i.imgur.com/y3GGAlX.png)

## Features

### Landing page

Introduces Likeminds, its purpose, and highlights the platform's mission of connecting STEM enthusiasts. Features a clean, Bootstrap-powered design with intuitive navigation, hero section with call-to-action buttons, and a comprehensive features showcase using modern card layouts.

### Book Clubs

-   **Create**: Comprehensive club creation form with sections for basic information, book/resource details, scheduling, club settings, and organizer information
-   **Browse**: Search and filter functionality allowing users to find clubs by subject (Physics, Mathematics, Programming, Engineering, Biology, Chemistry) and difficulty level (Beginner to Graduate)
-   **Details**: Each club displays member count, meeting times, difficulty level, and detailed descriptions
-   **Customization**: Club organizers can set privacy levels, approval requirements, prerequisites, and member expectations

### Newsletter System

-   **Signup Integration**: Newsletter modal accessible from footer on all pages
-   **Launch Notifications**: Dedicated signup page for early access notifications with interest-based preferences
-   **Privacy-Focused**: Clear consent mechanisms and unsubscribe options

### Navigation & User Experience

-   **Consistent Header**: Fixed navigation with active state indicators across all pages
-   **Smart Footer**: Comprehensive footer with quick links, contact information, and newsletter signup
-   **Error Handling**: Custom 404 page with helpful guidance and multiple pathways back to content

### Design Philosophy

-   **Clean Layout**: Focus on minimalism, prettiness and utility.
-   **Consistent Navigation**: Minimal navbar, with the feature to scroll back to it from the footer
-   **Color Scheme**:
    -   Primary brand color: `#2b2724` (dark brown/charcoal)
    -   Secondary color: `#37353b` (dark purple-gray)
    -   Highlight color: `#a0c9c0` (teal/mint green)
    -   Highlight light: `#dafffd` (very light teal)
    -   Background: `#fffef6` (warm white)
-   **Typography**:
    -   Heading font: `"cmu", sans-serif` - Computer Modern font family, widely recognized in STEM academia (especially TeX/LaTeX documents)
    -   Body font: `"Source Sans 3", sans-serif` - Clean, readable Source Sans 3 to promote the websites friendliness towards new learners.
    -   Fallback fonts: `"Fira Sans"` and system sans-serif stack
    -   Font size: Base 1.2rem for enhanced readability
    -   Clear spacing and hierarchy for readability.

### Accessibility Features

-   Semantic HTML for screen readers.
-   Minimal clutter and layout, with an accessible main content font.
-   Simple transitions, avoiding overstimulation.
-   High contrast text/backgrounds for accessibility.

---

## Testing

**Manual Testing**

-   **Responsive Design**: Verified Bootstrap grid system works correctly across mobile (320px+), tablet (768px+), and desktop (1200px+) viewports
-   **Navigation**: Tested all navigation links, active states, and mobile hamburger menu functionality - no dead links found
-   **Forms**: Validated club creation form, newsletter signup, and launch notification signup with proper validation and user feedback
-   **Interactive Elements**: Confirmed pagination styling, search/filter functionality, and modal operations work as expected
-   **Cross-Page Consistency**: Verified consistent header, footer, and styling across all pages (index, clubs, create, signup, error)

**Browser Testing**

-   **Firefox**: Full functionality verified across all features
-   **Helium**: Complete testing suite passed
-   **Chrome**: Layout and interactive elements working correctly
-   **Safari**: Responsive design and form functionality confirmed

**Accessibility Testing**

-   **Screen Reader**: Semantic HTML structure supports assistive technologies
-   **Keyboard Navigation**: All interactive elements accessible via keyboard
-   **Color Contrast**: Text/background combinations meet WCAG guidelines
-   **Focus Indicators**: Clear visual focus states for form elements and links

**Validators**

-   **W3C HTML**: Validation pending - all pages to be tested for semantic correctness
-   **W3C CSS**: Validation pending - custom stylesheet and Bootstrap overrides to be verified
-   **WCAG Accessibility**: Compliance testing pending - full accessibility audit planned

---

## Known Bugs

-   **Hero Section**: Hero text on the landing page can change length dramatically at specific Bootstrap breakpoints (particularly around 768px and 992px), causing layout shifts
-   **Footer Layout**: Footer components may organize erratically on very small screen sizes (below 320px), with social links and contact information potentially overlapping
-   **Form Validation**: Club creation form may not properly highlight all required fields on first submission attempt
-   **Pagination**: Custom pagination styling may not override Bootstrap defaults in all browser configurations

## Future Enhancements

-   **User Authentication**: Full user registration and login system for personalized club management
-   **Calendar Integration**: Sync club meeting schedules with popular calendar applications
-   **Progress Tracking**: Reading progress indicators and milestone achievements
-   **Content Management**: Admin panel for managing clubs, users, and site content

## Technologies Used

-   **Frontend**: HTML5, CSS3, JavaScript (ES6+)
-   **Framework**: Bootstrap 5.3.8 for responsive design and components
-   **Icons**: FontAwesome 6.4.0 for consistent iconography
-   **Fonts**: Google Fonts (Source Sans 3, Computer Modern) with Fira Sans and Sans-Serif fallbacks
-   **Version Control**: Git with GitHub repository hosting
-   **Development**: VS Code with live server for local development

## Deployment

-   **Platform**: GitHub Pages
-   **CDN**: Bootstrap and FontAwesome served via CDN for optimal performance

---
