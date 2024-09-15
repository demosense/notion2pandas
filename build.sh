#!/bin/bash
set -e
set -o pipefail

instruction()
{
  echo -e "usage: ./build.sh command <params> "
  echo -e 
  echo -e "Available commands:"
  echo -e
  echo -e "test"
  echo -e
}

# Parse options in format --arg value.
POSITIONAL=()
while [[ $# -gt 0 ]]
do
  key="$1"

  case $key in

      *)    # unknown option
        POSITIONAL+=("$1") # save it in an array for later
        shift # past argument
      ;;
  esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters

# There only one positional arg that is the command:
COMMAND=$1
if [ $# -eq 0 ]; then
  instruction
  exit 1
fi

# Run commands
case $COMMAND in

  test)
    pytest -vsx tests
  ;;

  *)
    echo -e "Unrecognized Command $COMMAND"
    echo -e
    instruction
    exit 1
  ;;

esac
