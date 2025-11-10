# ShiftViewer - Changelog

## Version 1.04 - November 10, 2025

### 🔍 New Features
- **Negative Search**: Exclude terms from search results using `-` prefix
  - Example: `TOC -RTOC` - Find TOC but exclude RTOC
  - Example: `unassigned -virtual` - Unassigned non-virtual shifts
  - Example: `wmr -john` - WMR shifts excluding John
  - Works with all search types (general, field-specific, quoted phrases)
  - Multiple exclusions supported: `-virtual -assigned`

### 🚀 Performance Improvements
- **Optimized Search Parsing**: Term parsing now happens once per search instead of per shift
  - Significantly faster for large datasets
  - Reduced memory usage
  - Better console logging for debugging

### 📚 Documentation
- Updated USER_GUIDE.html with negative search examples
- Added search syntax cheat sheet entries for exclusion
- Updated version to 1.04

---

## Version 1.03 - November 8, 2025

### Overview
Major enhancements to the ShiftViewer application improving search capabilities, UI/UX, data persistence, and overall usability.

---

## 🔍 Search Enhancements

### Advanced Search Syntax
- **Field-Specific Search**: Search within specific fields using `field:value` syntax
  - `name:John` - Search only in names
  - `role:WMR` - Search only in roles
  - `venue:RTOC` - Search only in venues
  - `date:15/11` - Search by date

### Multi-Criteria Search
- **Multiple Fields**: Combine multiple field searches
  - Example: `name:Olena venue:RTOC` - Find Olena at RTOC venue
  - All field criteria must match (AND logic)

### AND Search with Spaces
- **Space-Separated Terms**: Multiple terms are treated as AND conditions
  - `wmr olena` - Shows shifts containing BOTH "wmr" AND "olena" (in any field)
  - Each term must match at least one field

### Quoted Phrase Search
- **Exact Phrase Matching**: Use quotes to search for exact phrases
  - `"duty manager"` - Searches for the exact phrase "duty manager"
  - `duty manager` (without quotes) - Searches for "duty" AND "manager" separately

### Smart Date Search
- **Flexible Date Formats**: Supports both EU and US date formats
  - `date:15/11` - Tries both 15th November and 11th May
  - `date:11/15` - Same as above
  - `date:15/11/2025` - Specific date with year
  - `date:15/11/25` - 2-digit year support (25 → 2025)

- **Intelligent Year Inference**: Automatically infers year when omitted
  - November-December → 2025
  - January-March → 2026
  - Other months → Current year

### Search Performance
- **Debounced Input**: 200ms delay after typing stops before search executes
  - Reduces lag while typing
  - Prevents unnecessary re-renders
  - Smoother user experience

---

## 🎯 Filter Improvements

### My Shifts Filter
- **Personal Filter**: New "My Shifts" button to filter your shifts
  - Enter your name in the text box
  - Click "My Shifts" to activate filter
  - Works with tab filters (e.g., "Upcoming" + "My Shifts" = your upcoming shifts)
  - Toggle on/off by clicking again
  - Name persists in localStorage

### Saved Search
- **Persistent Searches**: Save frequently used searches
  - Enter search in "This search will be saved" box
  - Automatically saved to localStorage
  - Click "Execute Saved Search" to apply
  - Toggle on/off functionality
  - Wider input box (250px) for longer searches

### Filter Cleanup
- **Removed Redundant Filters**: Simplified UI by removing:
  - "All Roles" dropdown (redundant with search)
  - "All Venues" dropdown (use search instead)
  - "Unassigned Only" dropdown (use search or visual indicators)

### Visual Filter Feedback
- **Color-Coded Buttons**: Clear indication of active/inactive state
  - Gray background (#f3f4f6) = Inactive
  - Purple background (#667eea) = Active
  - Button text always black
  - Input text gray when inactive, black when active

---

## 💾 Data Persistence

### Local Storage
- **Shift Data Caching**: Save parsed shift data to browser
  - Avoid re-uploading Excel files
  - "Load Saved Data" button on landing page
  - Instant loading of previously uploaded data

### Persistent Preferences
- **Saved Settings**: User preferences persist across sessions
  - My name (for "My Shifts" filter)
  - Saved search query
  - All stored in localStorage

### Last Update Display
- **Consistent Timestamps**: Show Excel file's last update time
  - Displayed in title bar when viewing shifts
  - Shown on landing page for saved data
  - Color-coded based on recency:
    - Green: Updated within 24 hours
    - Orange: Updated 24-48 hours ago
    - Red: Updated more than 48 hours ago

---

## 🎨 UI/UX Improvements

### Shift Card Redesign
- **Compact Layout**: More information in less space
  - Reduced vertical spacing (30% more compact)
  - Grid layout for shift details
  - Responsive design adapts to screen size

### Card Header
- **Clear Hierarchy**: Name and role prominently displayed
  - Large, bold name (17px)
  - Role in purple below name
  - Status badge (Assigned/Unassigned) on the right
  - Color-coded badges (green/orange)

### Organized Details
- **Grid Layout**: Even spacing and alignment
  - Date, Venue, Location, Time (CET), Time (IST), Type
  - Small uppercase labels with icons
  - Consistent font sizes and spacing
  - Auto-fit grid (180px minimum per column)

### Contact Information
- **Horizontal Layout**: All contact info in one line
  - Teams Chat link (opens desktop app if installed)
  - Email address in gray
  - Individual phone (📱) - Personal phone number
  - Role phone (🔄) - Shared device passed between shifts
  - Separated by bullet points (•)
  - Compact gray background box

### Teams Integration
- **Desktop App Support**: Teams links now use `msteams://` protocol
  - Opens desktop Teams client if installed
  - Falls back to web version if not available
  - Direct chat links with shift assignees

### Phone Number Labels
- **Clear Distinction**: Better labels for phone types
  - **📱 Individual**: Personal phone number (always with the person)
  - **🔄 Role**: Shared phone (passed between shifts)
  - Hover tooltips explain each type

---

## 📱 Interactive Help

### Hover Tooltips
- **Contextual Help**: Information appears on hover (no click needed)
  - Search info button: Explains all search syntax
  - My Name info button: Explains personal filter
  - Phone numbers: Explains individual vs role phones
  - Positioned near their respective buttons

### Search Placeholder
- **Helpful Hints**: Placeholder text guides users
  - "Search shifts... (hover over blue i for more info)"
  - Directs users to help information

---

## 🐛 Bug Fixes

### Excel Parsing
- **COLE Format Support**: Properly handles COLE shift schedule format
  - Correct date parsing from Excel serial numbers
  - Proper column mapping
  - Handles both weekly and daily shift formats

### Date Handling
- **Duplicate Function Removal**: Fixed date parsing conflicts
  - Removed old `parseSearchDate` function
  - Single source of truth for date parsing
  - Consistent behavior across all date searches

### Search Logic
- **Field:Value Parsing**: Fixed regex to properly extract search criteria
  - Handles incomplete syntax gracefully
  - Ignores empty field:value pairs
  - Proper handling of special characters

---

## 📊 Technical Improvements

### Code Organization
- **Cleaner Codebase**: Removed redundant code
  - Eliminated duplicate functions
  - Consolidated filter logic
  - Removed unused DOM references

### Performance
- **Optimized Rendering**: Faster shift display
  - Debounced search input
  - Efficient filtering algorithms
  - Minimal re-renders

### Browser Compatibility
- **localStorage Instead of Cookies**: Better security and compatibility
  - Works with local file:// protocol
  - No browser security restrictions
  - Larger storage capacity

---

## 📝 Summary Statistics

- **Lines Changed**: 1,037 insertions, 277 deletions
- **Major Features Added**: 10+
- **Bugs Fixed**: 5+
- **UI Components Redesigned**: 3 (shift cards, filters, buttons)
- **Search Capabilities**: 6 new search types

---

## 🚀 Getting Started

### Using the New Features

1. **Search for shifts**:
   - Type in the search box
   - Use `field:value` for specific searches
   - Separate terms with spaces for AND search
   - Use quotes for exact phrases

2. **Filter your shifts**:
   - Enter your name in "My name" box
   - Click "👤 My Shifts" to activate
   - Click again to deactivate

3. **Save common searches**:
   - Type search in "This search will be saved" box
   - Click "Execute Saved Search" to apply
   - Toggle on/off as needed

4. **Load saved data**:
   - Click "Load Saved Data" on landing page
   - Instantly access previously uploaded shifts
   - No need to re-upload Excel file

---

## 💡 Tips & Tricks

- Hover over blue (i) buttons for help
- Use quotes for multi-word phrases: `"duty manager"`
- Combine search types: `role:WMR date:15/11 olena`
- Toggle filters on/off by clicking again
- Your preferences are automatically saved

---

## 🔮 Future Enhancements

Potential improvements for consideration:
- Export filtered results to Excel
- Calendar view of shifts
- Email notifications for upcoming shifts
- Mobile app version
- Multi-user collaboration features

---

**Current Version**: 1.04  
**Latest Release Date**: November 10, 2025  
**Repository**: https://github.com/maccorless/ShiftViewer
