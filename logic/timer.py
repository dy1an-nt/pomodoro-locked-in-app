class Timer:

    """Manages Pomodoro work and break session countdowns."""
    def __init__(self, work_duration: int = 25, break_duration: int = 5):
        self.work_duration: int = work_duration
        self.break_duration: int = break_duration
        self.seconds_left: int = self.work_duration * 60
        self.is_running: bool = False
        self.is_work_session: bool = True

    def start(self):
        if self.is_running:
            return
        self.is_running = True

    def pause(self):
        if not self.is_running:
            return
        self.is_running = False

    def reset(self):
        self.seconds_left: int = self.work_duration * 60
        self.is_running: bool = False
        self.is_work_session: bool = True


    def tick(self):
        if not self.is_running:
            return

        self.seconds_left -= 1

        if self.seconds_left == 0:
            self.is_work_session = not self.is_work_session
            if self.is_work_session:
                self.seconds_left = self.work_duration * 60
            else:
                self.seconds_left = self.break_duration * 60
        
            
        

