import plotly.figure_factory as ff

tasks = [
    dict(Task="Collect Requirements", Start='2023-01-22', Finish='2023-02-04'),
    dict(Task="Create Use Case Diagrams", Start='2023-02-11', Finish='2023-02-18'),
    dict(Task="Build Activity Diagrams for Each Use Case", Start='2023-02-15', Finish='2023-03-09'),
    dict(Task="Research User Interface Designs", Start='2023-02-27', Finish='2023-03-07'),
    dict(Task="Build Class Diagram", Start='2023-03-01', Finish='2023-03-09'),
    dict(Task="Get Customer Approval", Start='2023-03-10', Finish='2023-03-11'),
    dict(Task="Build Interface", Start='2023-03-12', Finish='2023-03-24'),
    dict(Task="Link DB to Interface", Start='2023-03-24', Finish='2023-04-03'),
    dict(Task="Build Business Logic", Start='2023-04-05', Finish='2023-04-27'),
    dict(Task="Test System", Start='2023-04-27', Finish='2023-05-07'),
    dict(Task="Deliver System", Start='2023-05-08', Finish='2023-05-09'),
    dict(Task="Sign-off Meeting", Start='2023-05-09', Finish='2023-05-10')
]

fig = ff.create_gantt(tasks, title = 'DriverPass Schedule')

fig.show()
