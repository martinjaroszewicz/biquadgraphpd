## Biquad Coefficient Converter for Pure Data

This Python script converts biquad filter coefficients for use with Pure Data's biquad~ object. It streamlines the process of implementing custom filters in Pure Data by automating the coefficient conversion.

![](https://github.com/biquadgraphpd/biquad2.gif)

### Features

- Graphs and converts standard biquad coefficients to Pure Data's biquad~ format
- Easy-to-use command-line interface
- Outputs coefficients ready for direct use in Pure Data patches

### Usage

1. Calculate your desired filter coefficients using the [BiQuadDesigner](https://arachnoid.com/BiQuadDesigner/) online tool.
2. Run the script with the calculated coefficients as arguments:

```bash
python filtercalc.py 
```

3. Copy the output coefficients into your Pure Data biquad~ object.

### Example

```bash
python biquad_converter.py 0.0675 0.1349 0.0675 -1.1430 0.4128
```

Output:
```
Pure Data biquad~ coefficients:
1.1430 -0.4128 0.0675 0.1349 0.0675 
```

### Requirements

- Python 3.x

### Notes

- The script automatically adjusts the signs of a1 and a2 coefficients to match Pure Data's convention.
- Always verify the converted coefficients in your Pure Data patch to ensure the desired filter response.

### Resources

- [BiQuadDesigner](https://arachnoid.com/BiQuadDesigner/): Online tool for calculating biquad filter coefficients

### License

This script is released under the MIT License. See the LICENSE file for details.

Citations:
[1] https://arachnoid.com/BiQuadDesigner/
