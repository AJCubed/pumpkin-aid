package com.pumpkin.prescreeningbe.repository;

import com.pumpkin.prescreeningbe.model.PreScreening;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface PreScreeningRepository extends JpaRepository<PreScreening, Long> {
    public List<PreScreening> findAllByName(String name);
}
