package com.example.psychetest

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.psychetest.databinding.ActivityMainBinding
import com.example.psychetest.databinding.ActivityRegistrationBinding

class MainActivity : AppCompatActivity() {

    private var binding: ActivityMainBinding? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)

        setContentView(binding?.root)

        binding?.OptA1?.setOnClickListener {
            navigateToQuestionTwo()
        }

        binding?.OptB1?.setOnClickListener {
            navigateToQuestionTwo()
        }

        binding?.OptC1?.setOnClickListener {
            navigateToQuestionTwo()
        }

        binding?.OptD1?.setOnClickListener {
            navigateToQuestionTwo()
        }

    }

    private fun navigateToQuestionTwo() {
        startActivity(Intent(this, QuestionTwo::class.java))
        finish()
    }
}