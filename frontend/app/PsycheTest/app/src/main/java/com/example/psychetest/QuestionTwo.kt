package com.example.psychetest

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.core.content.ContextCompat.startActivity
import com.example.psychetest.databinding.ActivityMainBinding
import com.example.psychetest.databinding.ActivityQuestionTwoBinding

class QuestionTwo : AppCompatActivity() {
    private var binding: ActivityQuestionTwoBinding? = null
    var calc = calc()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityQuestionTwoBinding.inflate(layoutInflater)
        setContentView(binding?.root)

        binding?.OptA2?.setOnClickListener {
            calc = addValues(calc, 0,0,10,0,0 )
            calc = subtractValue(calc, 0,0,0,20,0 )
            navigateToQuestionTwo()
        }

        binding?.OptB2?.setOnClickListener {
            calc = addValues(calc, 10,0,0,10,0 )
            calc = subtractValue(calc, 0,0,5,0,0 )
            navigateToQuestionTwo()
        }

        binding?.OptC2?.setOnClickListener {
            calc = subtractValue(calc, 0,0,20,0,0 )
            navigateToQuestionTwo()
        }

        binding?.OptD2?.setOnClickListener {
            calc = addValues(calc, 0,0,0,0,20 )
            calc = subtractValue(calc, 0,10,0,0,0 )
            navigateToQuestionTwo()
        }
    }

    private fun navigateToQuestionTwo() {
        startActivity(Intent(this, QuestionThree::class.java))
        finish()
    }

    fun addValues(data: calc, addition1: Int, addition2: Int, addition3: Int, addition4: Int, addition5: Int): calc {
        val newValue1 = data.O + addition1
        val newValue2 = data.C + addition2
        val newValue3 = data.E + addition3
        val newValue4 = data.A + addition4
        val newValue5 = data.N + addition5
        return data.copy(O = newValue1, C = newValue2, E = newValue3, A = newValue4, N = newValue5)
    }

    fun subtractValue(data: calc, subtraction1: Int, subtraction2: Int, subtraction3: Int, subtraction4: Int, subtraction5: Int): calc {
        val newValue1 = data.O - subtraction1
        val newValue2 = data.C - subtraction2
        val newValue3 = data.E - subtraction3
        val newValue4 = data.A - subtraction4
        val newValue5 = data.N - subtraction5
        return data.copy(O = newValue1, C = newValue2, E = newValue3, A = newValue4, N = newValue5)
    }
}