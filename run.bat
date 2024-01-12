pytest -vs -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
pytest -vs -m "sanity" --html=./Reports/report1.html testCases/ --browser firefox

rem pytest -vs -m "sanity and regression" --html=./Reports/report.html testCases/ --browser chrome
rem pytest -vs -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome
rem pytest -vs -m "regession" --html=./Reports/report.html testCases/ --browser chrome
rem pytest -vs -m "sanity and regression" --html=./Reports/report.html testCases/ --browser firefox
rem pytest -vs -m "sanity or regression" --html=./Reports/report.html testCases/ --browser firefox
rem pytest -vs -m "regession" --html=./Reports/report.html testCases/ --browser firefox
