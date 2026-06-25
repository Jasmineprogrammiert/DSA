# Problem 42.5 - Parallel Compilation
# A compiler needs to compile n packages (0 to n-1). Given an array of n
# positive integers, seconds, where seconds[i] is the time to compile
# package i, and an array imports where imports[i] is the list of packages
# that package i depends on, determine the minimum time to compile the
# entire program.
#
# - No circular dependencies.
# - Cannot start compiling until all dependencies finish.
# - No limit on parallel compilation if no dependencies between packages.
# - Program is fully compiled when all packages are compiled.
#
# Example 1:
# seconds = [10, 20, 30]
# imports = [[], [], [0, 1]]
# Output: 50
#
# Example 2:
# seconds = [10, 20, 30]
# imports = [[], [], []]
# Output: 30