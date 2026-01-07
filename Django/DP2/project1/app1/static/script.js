const employees = [
    { name: "Amit", title: "Software Developer", salary: 50000, fullTime: true },
    { name: "Sneha", title: "UI Designer", salary: 35000, fullTime: false },
    { name: "Rahul", title: "Tester", salary: 30000, fullTime: true }
];

const employeeList = document.getElementById("employeeList");

if (employees.length === 0) {
    employeeList.innerHTML = "<li>No employees available.</li>";
} else {
    for (let emp of employees) {
        const li = document.createElement("li");

        let statusText = emp.fullTime
            ? "<span class='full-time'>Full-Time</span>"
            : "<span class='part-time'>Part-Time</span>";

        li.innerHTML = `
            ${emp.name} - ${emp.title} - ₹${emp.salary} (${statusText})
        `;

        employeeList.appendChild(li);
    }
}
