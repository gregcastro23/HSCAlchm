import { Flame, Leaf, Droplets, Wind } from 'lucide-react'
import { ElementalBalance } from '../types/recipe'

interface ElementalBalanceChartProps {
  balance: ElementalBalance
}

export default function ElementalBalanceChart({ balance }: ElementalBalanceChartProps) {
  const elements = [
    { name: 'Fire', value: balance.Fire, color: 'bg-red-500', icon: Flame },
    { name: 'Earth', value: balance.Earth, color: 'bg-amber-500', icon: Leaf },
    { name: 'Water', value: balance.Water, color: 'bg-blue-500', icon: Droplets },
    { name: 'Air', value: balance.Air, color: 'bg-green-500', icon: Wind },
  ]

  return (
    <div className="space-y-4">
      {/* Visual Chart */}
      <div className="relative h-32 bg-stone-100 rounded-lg overflow-hidden">
        <div className="absolute inset-0 flex">
          {elements.map((element, index) => {
            const width = `${element.value * 100}%`
            const IconComponent = element.icon

            return (
              <div
                key={element.name}
                className={`h-full ${element.color} flex items-center justify-center relative group`}
                style={{ width }}
              >
                <IconComponent className="h-6 w-6 text-white opacity-80" />
                <div className="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 px-2 py-1 bg-stone-800 text-white text-xs rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">
                  {element.name}: {(element.value * 100).toFixed(0)}%
                </div>
              </div>
            )
          })}
        </div>
      </div>

      {/* Element Labels */}
      <div className="grid grid-cols-2 gap-3 text-sm">
        {elements.map((element) => {
          const IconComponent = element.icon
          return (
            <div key={element.name} className="flex items-center">
              <IconComponent className={`h-4 w-4 mr-2 ${element.color.replace('bg-', 'text-')}`} />
              <span className="text-stone-700">{element.name}</span>
              <span className="ml-auto font-medium text-stone-900">
                {(element.value * 100).toFixed(0)}%
              </span>
            </div>
          )
        })}
      </div>
    </div>
  )
}
