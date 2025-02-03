package com.example.soilapp.controller;

import com.example.soilapp.entity.FertilizerInput;
import com.example.soilapp.service.FertilizerInputService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/fertilizer")
public class FertilizerController {

    @Autowired
    private FertilizerInputService fertilizerInputService;

    // POST method to save data to the database
    @PostMapping("/predict")
    public ResponseEntity<FertilizerInput> createFertilizerInput(@RequestBody FertilizerInput fertilizerInput) {
        // Logic to calculate fertilizer recommendation and moisture prediction
        String fertilizerRecommendation = predictFertilizerRecommendation(fertilizerInput);
        float moisturePrediction = predictMoisture(fertilizerInput);

        // Set the values in the FertilizerInput object
        fertilizerInput.setFertilizerRecommendation(fertilizerRecommendation);
        fertilizerInput.setMoisturePrediction(moisturePrediction);

        // Save the input data to the database
        FertilizerInput savedInput = fertilizerInputService.saveFertilizerInput(fertilizerInput);

        return ResponseEntity.ok(savedInput);
    }

    // GET method to retrieve all stored data from the database
    @GetMapping("/inputs")
    public List<FertilizerInput> getAllFertilizerInputs() {
        return fertilizerInputService.getAllFertilizerInputs();
    }

    // Sample logic for fertilizer recommendation (you should use actual model or calculations)
    private String predictFertilizerRecommendation(FertilizerInput fertilizerInput) {
        // Example logic for fertilizer recommendation
        // Replace with your ML model prediction or logic
        return "Fertilizer Type 1";
    }

    // Sample logic for moisture prediction (you should use actual model or calculations)
    private float predictMoisture(FertilizerInput fertilizerInput) {
        // Example logic for moisture prediction
        // Replace with your ML model prediction or calculation
        return 15.5f;
    }
}
