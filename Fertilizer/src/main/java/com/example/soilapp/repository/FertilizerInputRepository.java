package com.example.soilapp.repository;

import com.example.soilapp.entity.FertilizerInput;
import org.springframework.data.jpa.repository.JpaRepository;

public interface FertilizerInputRepository extends JpaRepository<FertilizerInput, Long> {
    // You can define custom queries here if needed, otherwise, JpaRepository provides basic CRUD methods
}
