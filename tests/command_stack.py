import unittest

from commands import (
    ExitGameCommand,
)
from main import (
    CommandStack,
)


class TestCommandStack(unittest.TestCase):
    """
    Tests for CommandStack
    """

    def setUp(self):
        self.stack = CommandStack(limit=2)

    def test_add_command_to_stack(self):
        exit_command = ExitGameCommand()

        self.stack.add(exit_command)
        self.assertEqual(len(self.stack._stack), 1)
        self.assertEqual(self.stack._stack[0], exit_command)

    def test_pop_command_from_stack(self):
        exit_command = ExitGameCommand()

        self.stack.add(exit_command)
        popped_command = self.stack.pop()

        self.assertEqual(popped_command, exit_command)
        self.assertEqual(len(self.stack._stack), 0)

    def test_limit_stack(self):
        exit_command_1 = ExitGameCommand()
        exit_command_2 = ExitGameCommand()
        exit_command_3 = ExitGameCommand()

        self.stack.add(exit_command_1)
        self.stack.add(exit_command_2)
        self.assertEqual(len(self.stack._stack), 2)

        self.stack.add(exit_command_3)
        self.assertEqual(len(self.stack._stack), 2)
        self.assertEqual(self.stack._stack[0], exit_command_2)
        self.assertEqual(self.stack._stack[1], exit_command_3)


if __name__ == '__main__':
    unittest.main()
