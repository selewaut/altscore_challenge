from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)


@app.route("/phase-change-diagram")
def phase_change_diagram():
    try:
        pressure = request.args.get("pressure", type=float)
        if pressure is None:
            return jsonify({"error": "Pressure parameter is required"}), 400

        app.logger.debug(f"Received pressure: {pressure}")

        if pressure >= 10:
            specific_volume_liquid = 0.0035
            specific_volume_vapor = 0.0035
            app.logger.debug(f"Specific volume liquid: {specific_volume_liquid}")
            app.logger.debug(f"Specific volume vapor: {specific_volume_vapor}")
            return jsonify(
                {
                    "specific_volume_liquid": specific_volume_liquid,
                    "specific_volume_vapor": specific_volume_vapor,
                }
            )
        elif pressure >= 0.5:
            liquid_params = (4061.224489795918, -4.2142857142857135)
            vapor_params = (-0.3317053656259897, 10.001160968779692)

            v_liquid = (pressure - liquid_params[1]) / liquid_params[0]
            v_vapor = (pressure - vapor_params[1]) / vapor_params[0]

            specific_volume_liquid = round(v_liquid, 5)
            specific_volume_vapor = round(v_vapor, 5)

            app.logger.debug(f"Specific volume liquid: {specific_volume_liquid}")
            app.logger.debug(f"Specific volume vapor: {specific_volume_vapor}")

            return jsonify(
                {
                    "specific_volume_liquid": specific_volume_liquid,
                    "specific_volume_vapor": specific_volume_vapor,
                }
            )
        else:
            # pressure cannot be less than 0.5
            return jsonify({"error": "Pressure must be at least 0.5"}), 400

    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
