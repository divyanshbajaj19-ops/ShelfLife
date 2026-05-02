---
name: Premium Indian SaaS
colors:
  surface: '#f3fcef'
  surface-dim: '#d4ddd0'
  surface-bright: '#f3fcef'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#edf6ea'
  surface-container: '#e8f0e4'
  surface-container-high: '#e2ebde'
  surface-container-highest: '#dce5d9'
  on-surface: '#161d16'
  on-surface-variant: '#3d4a3d'
  inverse-surface: '#2a322a'
  inverse-on-surface: '#ebf3e7'
  outline: '#6d7b6c'
  outline-variant: '#bccbb9'
  surface-tint: '#006e2f'
  primary: '#006e2f'
  on-primary: '#ffffff'
  primary-container: '#22c55e'
  on-primary-container: '#004b1e'
  inverse-primary: '#4ae176'
  secondary: '#006d30'
  on-secondary: '#ffffff'
  secondary-container: '#92f5a4'
  on-secondary-container: '#007233'
  tertiary: '#9e4036'
  on-tertiary: '#ffffff'
  tertiary-container: '#ff8b7c'
  on-tertiary-container: '#76231b'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#6bff8f'
  primary-fixed-dim: '#4ae176'
  on-primary-fixed: '#002109'
  on-primary-fixed-variant: '#005321'
  secondary-fixed: '#95f8a7'
  secondary-fixed-dim: '#79db8d'
  on-secondary-fixed: '#00210a'
  on-secondary-fixed-variant: '#005323'
  tertiary-fixed: '#ffdad5'
  tertiary-fixed-dim: '#ffb4a9'
  on-tertiary-fixed: '#410001'
  on-tertiary-fixed-variant: '#7f2a21'
  background: '#f3fcef'
  on-background: '#161d16'
  surface-variant: '#dce5d9'
typography:
  h1:
    fontFamily: Be Vietnam Pro
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Be Vietnam Pro
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h3:
    fontFamily: Be Vietnam Pro
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  container-padding: 24px
  gutter: 16px
  card-gap: 20px
  section-margin: 48px
---

## Brand & Style
This design system embodies a "Modern Indian SaaS" aesthetic—a blend of high-utility performance and premium consumer delight. It draws inspiration from the precision of Zerodha and the immersive, card-based motion design of CRED. The objective is to make food inventory management feel less like a chore and more like a high-end lifestyle choice.

The style is characterized by **Futuristic Minimalism** with a **Glassmorphic** layer. It utilizes hyper-clean layouts, significant whitespace, and "soft-touch" interactions. The brand personality is eco-conscious (growth), mathematically precise (tracking), and culturally vibrant (alertness).

## Colors
The palette is rooted in a "Fresh Growth" philosophy. The **Primary Green** represents vitality and the reduction of waste, while the **Dark Green** is used for heavy-weight elements like primary navigation or deep-action headers to establish trust.

**Saffron/Yellow** is the system's "pulse"—it is used sparingly for expiry alerts and critical calls to action, providing a vibrant Indian contrast to the cool greens. The background uses a sophisticated light gray to make white "2xl" cards pop, creating a layered, physical feel.

## Typography
The system uses **Be Vietnam Pro** for headings to provide a friendly yet contemporary geometric structure (as a highly accessible alternative to Poppins). **Inter** is the workhorse for body text, ensuring maximum readability for complex data tables and inventory lists.

Headings should always use a tighter letter-spacing to feel "locked" and premium. Labels for expiry dates should prioritize clarity and use the `label-caps` style to differentiate metadata from core content.

## Layout & Spacing
The layout follows a **Fixed-Fluid Hybrid** model. On desktop, content is constrained to a 1280px max-width container to maintain the premium "editorial" feel, while on mobile it uses a 16px safe margin. 

The rhythm is based on an 8pt grid, but with "breathing gaps" (20px-24px) between dashboard cards to ensure the soft shadows do not overlap awkwardly. Grouped information (e.g., an item name and its expiry date) should use a tight 4px or 8px vertical stack.

## Elevation & Depth
Depth is created through **Ambient Shadowing** rather than harsh outlines. Cards utilize a "floating" effect with a 15% opacity Primary Green or Neutral tint in the shadow to make the UI feel alive.

**Glassmorphism** is applied to top navigation bars and bottom mobile docks using a 20px backdrop blur and a 1px semi-transparent white border. This ensures that as the user scrolls, the vibrant colors of the food items are subtly visible beneath the interface, maintaining a sense of spatial awareness.

## Shapes
The design system uses a **2xl roundedness (24px)** for all primary dashboard cards to evoke a friendly, consumer-tech feel. Buttons use a more aggressive **Pill-shape** (full round) to signify "interactive" versus "container."

Small components like checkboxes and status badges use a 12px (rounded-lg) radius to maintain harmony with the larger cards without appearing overly circular.

## Components

### Dashboard Cards
White backgrounds, `24px` corner radius, and a `1px` stroke in `#E5E7EB`. They must feature a subtle hover transition where the shadow deepens and the card lifts by `4px`.

### Primary Buttons
High-contrast `#22C55E` background with white text. Use a heavy horizontal padding (`32px`) and a slight `4px` bottom-glow shadow of the same color.

### Status Badges (Expiry Alerts)
Soft-tinted backgrounds with high-saturation text:
- **Fresh:** Background `success_tint`, Text `#15803D`.
- **Expiring Soon:** Background `warning_tint`, Text `#B45309`.
- **Expired:** Background `error_tint`, Text `#B91C1C`.

### Input Fields
Large, `16px` padded fields with a `#F9FAFB` fill. On focus, the border transitions to Primary Green with a `4px` soft outer glow.

### Glass Navigation
Top headers must have `backdrop-filter: blur(20px)` and a background of `rgba(255, 255, 255, 0.8)`. This keeps the "Shelf-Life" app feeling airy and futuristic.