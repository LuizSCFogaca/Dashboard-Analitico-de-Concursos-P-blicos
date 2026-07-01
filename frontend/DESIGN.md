---
name: RS Concursos Analytics
colors:
  surface: '#0d150e'
  surface-dim: '#0d150e'
  surface-bright: '#323c33'
  surface-container-lowest: '#081009'
  surface-container-low: '#151e16'
  surface-container: '#19221a'
  surface-container-high: '#232c24'
  surface-container-highest: '#2e372e'
  on-surface: '#dbe5d9'
  on-surface-variant: '#bacbb9'
  inverse-surface: '#dbe5d9'
  inverse-on-surface: '#29332a'
  outline: '#859585'
  outline-variant: '#3b4a3d'
  surface-tint: '#00e475'
  primary: '#75ff9e'
  on-primary: '#003918'
  primary-container: '#00e676'
  on-primary-container: '#00612e'
  inverse-primary: '#006d35'
  secondary: '#45fec9'
  on-secondary: '#003829'
  secondary-container: '#00e1ae'
  on-secondary-container: '#005e47'
  tertiary: '#ffdec4'
  on-tertiary: '#4b2800'
  tertiary-container: '#ffba79'
  on-tertiary-container: '#794810'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#62ff96'
  primary-fixed-dim: '#00e475'
  on-primary-fixed: '#00210b'
  on-primary-fixed-variant: '#005226'
  secondary-fixed: '#45fec9'
  secondary-fixed-dim: '#00e1ae'
  on-secondary-fixed: '#002117'
  on-secondary-fixed-variant: '#00513d'
  tertiary-fixed: '#ffdcbf'
  tertiary-fixed-dim: '#fdb878'
  on-tertiary-fixed: '#2d1600'
  on-tertiary-fixed-variant: '#6a3c03'
  background: '#0d150e'
  on-background: '#dbe5d9'
  surface-variant: '#2e372e'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-bold:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-padding: 24px
  gutter: 16px
  sidebar-width: 280px
  comparison-width: 320px
  stack-sm: 8px
  stack-md: 16px
---

## Brand & Style
The design system focuses on a high-utility, data-centric environment for candidates preparing for civil service exams in Rio Grande do Sul. The brand personality is **authoritative, analytical, and efficient**. It aims to evoke a sense of focus and professional seriousness, stripping away distractions to prioritize information density and clarity.

The visual style is **Corporate / Modern** with a lean toward **Minimalism**. It utilizes a "Dark Mode Only" approach to reduce eye strain during long research sessions. The aesthetic relies on flat surfaces, subtle borders for containment, and high-energy green accents to guide the user's eye toward calls-to-action and key data points.

## Colors
The palette is built on a foundation of deep charcoal and grays to maintain professional gravity. 
- **Primary:** A vibrant "Electric Green" (#00E676) is used exclusively for success states, primary buttons, and critical highlights.
- **Secondary:** A teal-leaning green (#1DE9B6) provides variety for data visualization and interactive elements like links.
- **Neutral:** The background is a solid deep charcoal (#121212). Surfaces (cards, sidebars) use #1E1E1E to create subtle depth without relying on shadows.
- **Borders:** A consistent #2C2C2C is used for structural separation, keeping the interface "flat" yet organized.

## Typography
We use **Inter** for its exceptional legibility in data-heavy environments. The type system prioritizes hierarchy through weight and scale. 
- **Headlines:** Use Bold and Semi-Bold weights for section titles and the main dashboard header.
- **Data Labels:** Small, uppercase bold labels are used for metadata (e.g., "SALÁRIO", "VAGAS") to differentiate titles from dynamic values.
- **Body:** Standardized at 14px for maximum information density in the 3-column layout without sacrificing readability.

## Layout & Spacing
The layout follows a **Fixed Grid** approach for the desktop dashboard to ensure the comparison tool remains anchored. 
- **Top Bar:** Fixed height (72px) containing title and global utilities.
- **3-Column Matrix:** 
    1. **Left (List):** Fixed width (280px). Scrollable list of cities.
    2. **Center (Detail):** Fluid width. This is the primary reading area.
    3. **Right (Comparison):** Fixed width (320px). A sticky tray for side-by-side analysis.
- **Rhythm:** An 8px base grid governs all internal padding. Use 16px gutters between columns to maintain clear visual boundaries.

## Elevation & Depth
In line with the flat design request, this design system avoids heavy shadows. Instead, it uses **Tonal Layers** and **Low-Contrast Outlines**:
- **Level 0 (Background):** #121212.
- **Level 1 (Cards/Panels):** #1E1E1E with a 1px border of #2C2C2C.
- **Level 2 (Hover States/Popovers):** #252525.
- **Interaction:** Active exam selection in the city list is indicated by a 4px left-border accent in Primary Green and a subtle background shift.

## Shapes
The shape language is **Soft**. A 4px (0.25rem) radius is applied to cards, input fields, and buttons. This creates a modern, slightly refined feel while maintaining the rigid structure necessary for a professional dashboard. Large buttons use `rounded-lg` (8px) to stand out as distinct interactive elements.

## Components
- **Buttons:** 
    - *Primary:* Solid Primary Green background with black text for maximum contrast.
    - *Secondary:* Outlined with Primary Green text.
- **Inputs & Filters:** Dark gray background (#252525) with a subtle #2C2C2C border. Focus state triggers a Primary Green border glow.
- **Data Cards:** Content in the center column is grouped by category (e.g., "Financials", "Requirements") using thin horizontal separators rather than nested cards to keep the UI clean.
- **Comparison Slots:** Empty states in the right column show a dashed border icon, prompting the user to "Add Exam to Compare."
- **Status Chips:** Small badges for status (e.g., "Inscrições Abertas") use the Secondary Green with 10% opacity background and full-color text.
- **Exam List Items:** High-density rows with "City Name" and "Number of Openings" as a secondary label.