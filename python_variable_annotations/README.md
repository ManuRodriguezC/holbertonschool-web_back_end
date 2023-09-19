# Annotations types.

In Python you can create different variables controlling or determining their possible data type. A good way to do this is using typing which allows you to specify the type of data you expect to receive and the type of data you expect to return.

This are some examples with how you can annotations

$def stringify(num: int) -> str:
$    return str(num)

# And here's how you specify multiple arguments
$def plus(num1: int, num2: int) -> int:
$    return num1 + num2
