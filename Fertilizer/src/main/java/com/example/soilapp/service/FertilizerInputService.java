package com.example.soilapp.service;

import com.example.soilapp.entity.FertilizerInput;
import com.example.soilapp.repository.FertilizerInputRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class FertilizerInputService {

    @Autowired
    private FertilizerInputRepository fertilizerInputRepository;

    // Save FertilizerInput to the database
    public FertilizerInput saveFertilizerInput(FertilizerInput fertilizerInput) {
        return fertilizerInputRepository.save(fertilizerInput);
    }

    // Retrieve all FertilizerInputs
    public List<FertilizerInput> getAllFertilizerInputs() {
        return fertilizerInputRepository.findAll();
    }
}
