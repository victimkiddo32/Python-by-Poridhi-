#git add . ; git commit -m "Backtracking" ; git push -u origin main


class Solution:
    def backtrack(self, curr_state):
        if self.is_goal(curr_state):
            self.record_solution(curr_state)
            return  # base case: stop recursion once goal is reached

        for choice in self.possible_choices(curr_state):
            if self.is_valid(choice, curr_state):
                self.make_choice(choice, curr_state)
                self.backtrack(curr_state)   # recursive call
                self.undo_choice(choice, curr_state)  # backtrack step

    def is_goal(self, curr_state):
        pass

    def record_solution(self, curr_state):
        pass

    def possible_choices(self, curr_state):
        pass

    def is_valid(self, choice, curr_state):
        pass

    def make_choice(self, choice, curr_state):
        pass

    def undo_choice(self, choice, curr_state):
        pass

#example usage:
if __name__=="__main__":
    initial_state={}
    sol=Solution()
    sol.backtrack(initial_state)


