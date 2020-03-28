DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )";
DURATIONS=5;

cd $DIR/..;
export PYTHONPATH=$(pwd);

echo "First check if code is properly formatted...";
flake8 beholder tests;
ok=$?;
if [ $ok -ne 0 ]; then
    echo "Code is not formatted properly. Please fix it and come back to me.";
    exit 1;
fi
echo "--------------------------------------------------------------------------"

echo "Now it's time to check if the unit tests are passing...";
pytest -vv --durations=$DURATIONS --cov="$PYTHONPATH/beholder" --cov-config="$PYTHONPATH/.coveragerc" --cov-report term-missing;

ok=$?;
if [ $ok -ne 0 ]; then
    echo "Unit tests failed. Please fix them..."
fi
echo "--------------------------------------------------------------------------"

echo "Finally, let's statically check the typing of your code";
mypy --ignore-missing-imports "$PYTHONPATH/beholder"
ok=$?;
if [ $ok -ne 0 ]; then
  echo "There are some problems with types. Fix them and come back..."
fi
echo "--------------------------------------------------------------------------"

echo "You are free to go. Remember that coverage should be as close to 100% as possible."
echo "Also, remember that unit tests shouldn't be too slow. $DURATIONS slowest tests are listed."
