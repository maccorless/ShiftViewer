# ShiftViewer Redesign Guide
## Olympic Winter Theme - Milano Cortina 2026

### Design Philosophy

**Olympic Winter Aesthetic**: Clean, modern, inspired by winter sports and the Olympic spirit
- Ice blue, deep navy, silver/white color palette
- Minimalist with generous whitespace
- Professional and trustworthy
- Subtle motion and polish

---

## Color Palette

```css
/* Olympic Winter Colors */
--ice-blue: #E3F2FD;        /* Background gradient start */
--sky-blue: #90CAF9;        /* Background gradient end */
--olympic-blue: #1976D2;    /* Primary actions */
--deep-navy: #0D47A1;       /* Primary dark */
--silver: #ECEFF1;          /* Borders, dividers */
--frost-white: #FAFAFA;     /* Input backgrounds */
--snow-white: #FFFFFF;      /* Card backgrounds */
--charcoal: #263238;        /* Primary text */
--slate: #546E7A;           /* Secondary text */
```

---

## Key Visual Changes

### 1. **Header**
- Gradient background: Deep navy → Olympic blue
- Large, bold title with Olympic rings subtle pattern
- "Milano Cortina 2026" branding
- Help link: Frosted glass effect with backdrop blur

### 2. **Typography**
- Font: Inter (Google Fonts) - clean, modern
- Weight hierarchy: 300/400/500/600/700
- Proper letter-spacing and line-height
- Size scale: 0.75rem → 2.5rem

### 3. **Cards (Shift Cards)**
- Elevated with soft shadows
- Hover effect: Lift up 2px, increase shadow
- Border radius: 12px (rounded corners)
- Clean grid layout for details
- Status badges: Pill-shaped with subtle backgrounds

### 4. **Buttons & Inputs**
- Rounded corners (6-12px)
- Gradient backgrounds for primary actions
- Hover states: Transform + shadow
- Focus states: Blue ring (accessibility)
- Disabled state: 50% opacity

### 5. **Filters Section**
- White card with subtle shadow
- Flexbox layout, wraps on mobile
- Info buttons: Circular, blue, hover scale
- Tooltips: Dark with blue accents

### 6. **Statistics Bar**
- Horizontal flex layout
- Large numbers in Olympic blue
- Icons + labels
- Responsive wrapping

---

## Spacing System

```css
--space-xs: 4px;
--space-sm: 8px;
--space-md: 16px;
--space-lg: 24px;
--space-xl: 32px;
--space-2xl: 48px;
```

---

## Shadow System

```css
--shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
--shadow-md: 0 4px 12px rgba(0,0,0,0.1);
--shadow-lg: 0 8px 24px rgba(0,0,0,0.12);
--shadow-xl: 0 12px 36px rgba(0,0,0,0.15);
```

---

## Animations

- **Transitions**: 150ms (fast), 250ms (base), 350ms (slow)
- **Hover effects**: translateY(-2px) + shadow increase
- **Card entrance**: fadeIn animation (0.3s)
- **Button press**: translateY(0) on active

---

## Responsive Breakpoints

- **Mobile**: < 768px
  - Stack filters vertically
  - Full-width buttons
  - Smaller header text
  - Single column cards

---

## Implementation Steps

1. Replace `<style>` section with new CSS
2. Update HTML class names to match new design
3. Keep all JavaScript unchanged
4. Test on mobile and desktop
5. Verify all functionality works

---

## Files to Modify

- `index.html` - Apply new styles and class names
- Keep all `<script>` sections identical
- Only change HTML structure and CSS

---

## Benefits

✅ Modern, professional appearance  
✅ Better visual hierarchy  
✅ Improved readability  
✅ Olympic branding  
✅ Smooth interactions  
✅ Mobile-friendly  
✅ Accessible (focus states, contrast)  

---

**Note**: The redesign is purely visual. All functionality, data handling, and logic remain unchanged.
