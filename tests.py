import pytest

from correct_stack import correct_stack


@pytest.mark.parametrize(
    "brackets",
    (
        ('(((([{}]))))'),
        ('[([])((([[[]]])))]{()}'),
        ('{{[()]}}')
    )
)
def test_correct_stack_positive(brackets):
    expected = 'Сбалансированно'
    assert correct_stack(brackets) == expected


@pytest.mark.parametrize(
    "brackets",
    (
        ('}{}'),
        ('{{[(])]}}'),
        ('[[{())}]')
    )
)
def test_correct_stack_negative(brackets):
    expected = 'Несбалансированно'
    assert correct_stack(brackets) == expected
