from csp import CSP, parse_neighbors, min_conflicts, backtracking_search, mrv, forward_checking

def Scheduler():

    Courses = 'cs108 cs112 cs212 cs214 cs262 cs232 cs384'.split()
    Professors = 'Adams VanderLinden Norman Schuurman Plantinga'.split()
    TimeSlots = 'mwf800 mwf900 mwf1030 mwf1130'.split()
    Classrooms = 'sb382 nh253'.split()

    values = []
    for time in TimeSlots:
        for classroom in Classrooms:
            for prof in Professors:
                values.append([time, classroom, prof])

    # Set up domains for each class
    domains = {}
    for var in Courses:
        domains[var] = values

    # Set up each class as a neighbor for the other classes
    neighbors = {}
    for type in [Courses]:
        for A in type:
            neighbors[A] = []
    for type in [Courses]:
        for A in type:
            for B in type:
                if A != B:
                    if B not in neighbors[A]:
                        neighbors[A].append(B)
                    if A not in neighbors[B]:
                        neighbors[B].append(A)

    def scheduler_constraint(A, a, B, b, recurse=0):
        prof_to_course = {
            'cs108': "Schuurman",
            'cs112': "Adams",
            'cs212': "Plantinga",
            'cs214': "Adams",
            'cs232': "Norman",
            'cs262': "VanderLinden",
            'cs384': "Schuurman"
        }
        if prof_to_course[A] != a[2] or prof_to_course[B] != b[2]:  # Prof isn't teaching the right course
            return False
        if a[2] == b[2] and a[0] == b[0]:  # Professor is the same and TimeSlot is the same
            return False
        if a[1] == b[1] and a[0] == b[0]:  # Classroom is the same and TimeSlot is the same
            return False
        return True
    return CSP(Courses, domains, neighbors, scheduler_constraint)


def print_solution(result):
    """A CSP solution printer copied from csp.py."""
    Courses = 'cs108 cs112 cs212 cs214 cs262 cs232 cs384'.split()
    for course in list(Courses):
        print('Course:', course)
        for (var, val) in result.items():
            if var == course:
                for i in val: print('\t', i)


if __name__ == "__main__":

    puzzle = Scheduler()
    result = backtracking_search(puzzle, select_unassigned_variable=mrv, inference=forward_checking)

    if puzzle.goal_test(puzzle.infer_assignment()):
        print("Solution:\n")
        print_solution(result)
    else:
        print("failed...")
        print(puzzle.curr_domains)
        puzzle.display(puzzle.infer_assignment())