package com.example.psychetest

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.psychetest.databinding.ActivityMainBinding
import com.example.psychetest.databinding.ActivityRegistrationBinding
import com.google.android.gms.common.data.DataBufferSafeParcelable.addValue

class MainActivity : AppCompatActivity() {

    private var binding: ActivityMainBinding? = null
    var calc = calc()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)

        setContentView(binding?.root)

        binding?.OptA1?.setOnClickListener {
            calc = addValues(calc, 0,20,0,0,0 )
            navigateToQuestionTwo()
        }

        binding?.OptB1?.setOnClickListener {
            calc = subtractValue(calc, 0,20,0,0,0 )
            navigateToQuestionTwo()

        }

        binding?.OptC1?.setOnClickListener {
            calc = addValues(calc, 15,0,0,0,0 )
            navigateToQuestionTwo()
        }

        binding?.OptD1?.setOnClickListener {
            calc = addValues(calc, 0,0,20,0,0 )
            navigateToQuestionTwo()
        }

    }

    private fun navigateToQuestionTwo() {
        startActivity(Intent(this, QuestionTwo::class.java))
        finish()
    }

    fun addValues(data: calc, o: Int, c: Int, e: Int, a: Int, n: Int): calc {
        val newValue1 = data.O + o
        val newValue2 = data.C + c
        val newValue3 = data.E + e
        val newValue4 = data.A + a
        val newValue5 = data.N + n
        return data.copy(O = newValue1, C = newValue2, E = newValue3, A = newValue4, N = newValue5)
    }

    fun subtractValue(data: calc, o: Int, c: Int, e: Int, a: Int, n: Int): calc {
        val newValue1 = data.O - o
        val newValue2 = data.C - c
        val newValue3 = data.E - e
        val newValue4 = data.A - a
        val newValue5 = data.N - n
        return data.copy(O = newValue1, C = newValue2, E = newValue3, A = newValue4, N = newValue5)
    }

}