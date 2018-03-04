from .users import Profile, Group
from .courses import Course, CourseSection, TimeSection
from .searches import SearchEntry, UserSearchEntry, GroupSearchEntry, Search, SearchResultsCache
from .data_tags import DataTag, SkillTag, LanguageTag, ConceptTag, FrameworkTag, LocationTag



# You Need in the Database:

# User Accounts (LoginView)
# Profile Data (Name, Courses, Location, Bio, Skills, Picture)
# -- Skills Tags (extend Languages, Frameworks, Concepts)
# -- Location Options

# Notifications per user?
#  -- New notifications?
#  Courses

# Search Criteria
# -- Course, Purpose (custom), Capacity, Skillsets (references skill tags), Description
# Search Results
# -- New Results (user for updates)
