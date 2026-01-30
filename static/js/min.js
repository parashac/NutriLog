document.addEventListener("DOMContentLoaded", function () {

    const ctx = document.getElementById("weeklyChart");

    if (ctx) {
        new Chart(ctx, {
            type: "bar",
            data: {
                labels: weeklyLabels,
                datasets: [{
                    label: "Calories Burned",
                    data: weeklyCalories,
                    backgroundColor: "#ff9f43"
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

});
