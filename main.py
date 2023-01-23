class Worker:
    def __init__(self, name, *args):
        self.name = name

        self._schedule = {
            "Sunday": False,
            "Monday": False,
            "Tuesday": False,
            "Wednesday": False,
            "Thursday": False,
            "Friday": False,
            "Saturday": False}

        self._daysoff = {
            "Sunday": False,
            "Monday": False,
            "Tuesday": False,
            "Wednesday": False,
            "Thursday": False,
            "Friday": False,
            "Saturday": False}
        # can I run set_days_off() here?
        for day in *args:
            assert day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            self._daysoff[day] = True

    @property
    def schedule(self):
        """Docstring for the 'schedule' property"""
        return self._schedule

    def add_to_schedule(self, *args):
        for day in *args:
            assert day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            if self._daysoff[day] == True:
                raise ValueError("Tried to add worker on their day off!")
            if self._schedule[day] == True:
                raise ValueError("Tried to add worker when they are already scheduled on this day!")
            self._schedule[day] = True

    def remove_from_schedule(self, *args):
        for day in *args:
            assert day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            self._schedule[day] = False

    def clear_schedule(self):
        self._schedule = {
            "Sunday": False,
            "Monday": False,
            "Tuesday": False,
            "Wednesday": False,
            "Thursday": False,
            "Friday": False,
            "Saturday": False}

    def set_days_off(self, *args):
        self._daysoff = {
            "Sunday": False,
            "Monday": False,
            "Tuesday": False,
            "Wednesday": False,
            "Thursday": False,
            "Friday": False,
            "Saturday": False}
        for day in *args:
            assert day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            self._daysoff[day] = True


class Server(Worker):
    def __init__(self, name):


class Bartender(Worker):
    def __init__(self, name):


class Cook(Worker):
    def __init__(self, name):


def update_schedules_of(day, *args):
    failures = 0
    for worker in *args:
        try:
            worker.add_to_schedule(day)
        except ValueError:
            print(f"Encountered a problem with {worker}!")
            failures += 1
    return failures


def assign_workers(day, *args):
    to_assign = []
    for group in *args:
        # this grabs first worker in each list and adds to schedule, revisit this
        to_assign.append(group[0])
    failures = update_schedules_of(day, to_assign.items())
    if failures != 0:
        pass  # explore the case where failures occur


# adding in script to make csv file
# def out_to_csv(self):
# pass
servers = []
frank = Server("Frank", "Monday", "Tuesday")
servers.append(frank)
# do this for each one
suze = Server("Suze", "Wednesday", "Thursday")
daniel = Server("Daniel", "Thursday", "Friday")
jordan = Server("Jordan", "Sunday", "Monday")

bartenders = []
pascal = Bartender("Pascal", "Monday", "Tuesday")
dante = Bartender("Dante", "Wednesday", "Thursday")
sky = Bartender("Sky", "Sunday", "Monday")

cooks = []
luis = Cook("Luis", "Monday", "Tuesday")
melissa = Cook("Melissa", "Wednesday", "Thursday")
emily = Cook("Emily", "Friday", "Saturday")

>>  # do this for all the names, remove the other stuff


frank.add_to_schedule("Sunday", "Monday", "Wednesday", "Thursday", "Friday")
suze.add_to_schedule("Friday", "Saturday", "Sunday", "Monday", "Tuesday")

