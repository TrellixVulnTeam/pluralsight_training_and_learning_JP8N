import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.Topology;
import org.apache.kafka.streams.kstream.KGroupedStream;
import org.apache.kafka.streams.kstream.KStream;
import org.apache.kafka.streams.kstream.KTable;
import org.apache.kafka.streams.kstream.TimeWindows;

import java.time.Duration;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

public class WindowingData {

	
	public static void main(String[] args) {
		Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "Weather_windowing");
        //Port 29092 is used because the docker compose file exposes that to our computer
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:29092");
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.Integer().getClass());
        props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
		
        long windowSizeMs = TimeUnit.MINUTES.toMillis(5); // 5 * 60 * 1000L
        
		StreamsBuilder builder = new StreamsBuilder();
		KStream<String, Integer> rawReadings = builder.stream("rawReadings");
		//KStream<String, Integer>[] averagedReadings = rawReadings.groupByKey().windowedBy(TimeWindows(windowSizeMs));
			      
		
		
		Topology topo = builder.build();
		
		KafkaStreams streams = new KafkaStreams(topo, props);
		streams.cleanUp();
		streams.start();
		
		Runtime.getRuntime().addShutdownHook(new Thread(streams::close));
	}

}
