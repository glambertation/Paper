#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutIteration(Koan):

    def test_iterators_are_a_type(self):
        # b = range(1,6)
        # print type(b)
        it = iter(range(1, 6))
        fib = 0

        for num in it:
            fib += num
            print num

        self.assertEqual(15, fib)

    def test_iterating_with_next(self):
        stages = iter(['alpha', 'beta', 'gamma'])

        try:
            self.assertEqual('alpha', next(stages))
            next(stages)
            self.assertEqual('gamma', next(stages))
            next(stages)
        except StopIteration as ex:
            err_msg = 'Ran out of iterations'

        self.assertMatch('Ran out of iterations', err_msg)

    # ------------------------------------------------------------------

    def add_ten(self, item):
        return item + 10

    def test_map_transforms_elements_of_a_list(self):
        seq = [1, 2, 3]

        mapped_seq = map(self.add_ten, seq)
        self.assertEqual([11,12,13], mapped_seq)

    def test_filter_selects_certain_items_from_a_list(self):
        def is_even(item):
            return (item % 2) == 0

        seq = [1, 2, 3, 4, 5, 6]

        even_numbers = filter(is_even, seq)
        self.assertEqual([2,4,6], even_numbers)

    def test_just_return_first_item_found(self):
        def is_big_name(item):
            return len(item) > 4

        names = ["Jim", "Bill", "Clarence", "Doug", "Eli"]

        # NOTE This still iterates through the whole names, so not particularly
        # efficient
        self.assertEqual(['Clarence'], filter(is_big_name, names)[:1])

        # Boring but effective
        for item in names:
            if is_big_name(item):
                self.assertEqual('Clarence', item)
                break

    # ------------------------------------------------------------------

    def add(self, accum, item):
        print 'pppp'
        print 'acc: '
        print accum
        print 'item: '
        print item
        return accum + item

    def multiply(self, accum, item):
        return accum * item

    def test_reduce_will_blow_your_mind(self):
        result = reduce(self.add, [2, 3, 4])
        self.assertEqual(9, result)

        result2 = reduce(self.multiply, [2, 3, 4], 2)
        self.assertEqual(48, result2)

        # Extra Credit:
        # Describe in your own words what reduce does.

    # ------------------------------------------------------------------

    def test_use_pass_for_iterations_with_no_body(self):
        for num in range(1, 5):
            pass

        self.assertEqual(4, num)

    # ------------------------------------------------------------------

    def test_all_iteration_methods_work_on_any_sequence_not_just_lists(self):
        # Ranges are an iterable sequence
        result = map(self.add_ten, range(1, 4))
        print "ee"
        print type(result)

        self.assertEqual([11,12,13], list(result))

        try:
            f = open("example_file.txt")

            try:
                def make_upcase(line):
                    return line.strip().upper()
                upcase_lines = map(make_upcase, f.readlines())
                self.assertEqual(['THIS', 'IS', 'A', 'TEST'], list(upcase_lines))
            finally:
                # Arg, this is ugly.
                # We will figure out how to fix this later.
                f.close()
        except IOError:
            # should never happen
            self.fail()
