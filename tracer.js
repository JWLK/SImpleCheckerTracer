const spawn = require("child_process").spawn;

const result = spawn("python", ["tracer.py", "images/sample_00.png"]);

result.stdout.on("data", (data) => {
    console.log(data.toString());
    var dataSplits = data.toString().split("\n", 3);
    console.log(dataSplits);
    var re = ",";
    var elements0 = dataSplits[0]
        .substring(1, dataSplits[0].length - 1)
        .split(re);
    var elements1 = dataSplits[1]
        .substring(1, dataSplits[1].length - 1)
        .split(re);
    var elements2 = dataSplits[2]
        .substring(1, dataSplits[2].length - 1)
        .split(re);

    console.log(elements0);
    console.log(elements1);
    console.log(elements2);
});

result.stderr.on("data", (data) => {
    console.log(data.toString());
});
